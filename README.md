# CSV Download Automation for Facebook Data from Crowdtangle
### Purpose
To extract data from Crowdtangle with selenium library.
### Pre-requisites
- Facebook account with Crowdtangle authentication access.
- Python 3.7
### Setup
- You can install required setups from pip;

    ``` commandline
    $ pip install -r requirements.txt
    ```

### Usage
- You can just fill the config.JSON file.

   ``` commandline
    {
  "SENTRY_TOKEN": " *sentry token address* ",
  "username": " *facebook username* ",
  "password": " *facebook password* "
    }
   ```

### Output
- You should be able to see  ``` "All CSV files are successfully sent to your inbox."``` message when the program finishes running, and extracted data from the Crowdtangle will be in your Facebook-linked mail inbox in ``` .csv ``` format. And you can fallow logs from under log directory.

### Known Issues
* Sometimes program stops running due to sleep time problems. Run the program again, and it will run without a problem.