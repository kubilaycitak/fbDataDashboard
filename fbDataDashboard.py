import self as self
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import sentry_sdk
import json
import logging

# Logging Initialization
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
LOGGER = logging.getLogger(self.__class__.__name__)

# Reading config.JSON file to capture the required data.
LOGGER.info('Reading config.JSON file to capture the required data.')
with open('config.json') as config_file:
    data = json.load(config_file)
SENTRY_TOKEN = data['SENTRY_TOKEN']
username = data['username']
password = data['password']

# Initializing Sentry
LOGGER.info('Initializing Sentry.')
sentry_sdk.init(SENTRY_TOKEN)

# Preparing the driver.
LOGGER.info('Preparing the driver.')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://apps.crowdtangle.com/datafacebook/lists/pages")
time.sleep(3)

# Finding login button in the main page and clicking it.
LOGGER.info('Finding login button.')
firstLoginButton = '//*[@id="account-react"]/div/div/div[2]/button/span'
firstLoginButton_element = driver.find_element_by_xpath(firstLoginButton)
firstLoginButton_element.click()

# Switching to the new opened page.
LOGGER.info('Switching to the new opened page.')
handles = driver.window_handles
driver.switch_to.window(handles[1])

# Finding the user name and password boxes in the newly opened page and filling them, then clicking login button.
LOGGER.info('Finding the user name and password boxes in the page.')
email_xpath = '//*[@id="email"]'
password_xpath = '//*[@id="pass"]'
login_button_xpath = '//*[@id="u_0_0"]'

email_element = driver.find_element_by_xpath(email_xpath)
password_element = driver.find_element_by_xpath(password_xpath)
login_button_element = driver.find_element_by_xpath(login_button_xpath)

LOGGER.info('Filling the boxes.')
email_element.send_keys(username)
password_element.send_keys(password)
login_button_element.click()

# Putting the program to sleep in order to be able to catch up with the main page handler.
LOGGER.info('Sleep time to catch main page handler.')
time.sleep(7)
driver.switch_to.window(handles[0])

# Getting the dashboard
LOGGER.info('Getting the dashboard.')
dashboardItems = '//*[@id="body-container-inner"]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[2]/div'
dashboardItems_element = driver.find_element_by_xpath(dashboardItems)

# Getting the dashboard's HTML code in order to reach every link inside it, and separating every one of them.
LOGGER.info('Getting the links from the dashboard.')
allURLs = dashboardItems_element.get_property('innerHTML')
urlList = allURLs.split("<a href=")
separator = ', '
separator.join(urlList)

# Obtaining pure links and putting them into an array. (Links themselves not used in the current algorithm.)
finalLinks = []
for i in range(1, len(urlList)):
    d = re.findall(r"([a-z/\d]*)", urlList[i])
    finalLinks.append(d[1])

# Clicking every link on dashboard.
LOGGER.info('Clicking the links.')
for i in range(1, len(finalLinks) + 1):
    linkToClick = '// *[ @ id = "body-container-inner"] / div[2] / div[4] / div[1] / div[2] / div[1] / div / div[2] / ' \
                  'div / span[' + str(i) + '] '
    linkToClick_element = driver.find_element_by_xpath(linkToClick)
    linkToClick_element.click()
    time.sleep(2)

    # While visiting every link in the dashboard, clicking the download buttons if they exist.
    try:
        LOGGER.info('Checking if download button exists in the page, if so clicking.')
        downloadButton = '/html/body/div[3]/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[8]/div[2]'
        downloadButton_element = driver.find_element_by_xpath(downloadButton)
        downloadButton_element.click()
        time.sleep(4)
    finally:
        continue

# Closing the driver and finishing the job.
LOGGER.info('Closing.')
driver.quit()

LOGGER.info('Success.')
print("All CSV files are successfully sent to your inbox.")