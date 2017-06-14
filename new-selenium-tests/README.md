# Installation:

- **Python** dependencies are listed on requirements.txt and can be installed by running:

  `pip install -r requirements.txt`

- Install [**chromedriver**](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    ```
    sudo apt-get install unzip

    wget -N http://chromedriver.storage.googleapis.com/2.30/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    chmod +x chromedriver

    sudo mv -f chromedriver /usr/local/share/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
    ```
- Install **Xvfb**:

  (on Linux: `apt-get install xvfb` )

# Running the tests

Set the values of the following environment variables:

- **KOBO_USERNAME**
- **KOBO_PASSWORD**
- **KOBOFORM_URL**

## Using Jenkins

In addition to the previous environment variables you need to set the following:

- **KOBO_SELENIUM_TESTS**: the location of the selenium tests
- **SELENIUM_BROWSER_VISIBLITY** (For running the browser in **_headless mode_** set it to **0**)

### Dependencies:

- [Chromedriver plugin](https://wiki.jenkins-ci.org/display/JENKINS/ChromeDriver+plugin)
- [ShiningPanda (Python Support)](https://wiki.jenkins-ci.org/display/JENKINS/ShiningPanda+Plugin)

### Running the tests using Jenkins:

Use the jenkins-selenium.sh file to run the tests on Jenkins
