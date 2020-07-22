# CSV Download Automation for Facebook Data from Crowdtangle
### Purpose
To extract data from Crowdtangle with selenium library.
### Pre-requisites
- Facebook account with Crowdtangle authentication access.
- Python 3.7
### Setup
- Make sure you have ``` Chromedriver ```  and ``` webdriver-manager ``` installed. If not, you can use pip;

    ``` commandline
    $ pip install chromedriver
    $ pip install webdriver-manager

    ```

#### Usage
Fill the config.JSON file.
   ``` commandline
    {
  "SENTRY_TOKEN": " *sentry token address* ",
  "username": " *facebook username* ",
  "password": " *facebook password* "
    }
   ```

#### Output
You should be able to see  ``` "All CSV files are successfully sent to your inbox."``` message when the program finishes running, and extracted data from the Crowdtangle will be in your Facebook-linked mail inbox in ``` .csv ``` format. And you can fallow logs from under log directory.

## Known Issues
* Sometimes program stops running due to sleep time problems. Run the program again, and it will run without a problem.