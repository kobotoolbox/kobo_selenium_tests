# Installation:
*  **Python** dependencies are listed on requirements.txt and can be installed by running:

    `pip install -r requirements.txt`
* Install [**chromedriver**](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* Install **Xvfb**:

    (on Linux: `apt-get install xvfb` )

# Running the tests
Set the values of the following environment variables:

* **KOBO_USERNAME**
* **KOBO_PASSWORD**
* **KOBOFORM_URL**

## Using Jenkins
In addition to the previous environment variables you need to set the following:
* **KOBO_SELENIUM_TESTS**:  the location of the selenium tests
* **SELENIUM_BROWSER_VISIBLITY** (For running the browser in ***headless mode*** set it to **0**)

#### Dependencies:
* [Chromedriver plugin](https://wiki.jenkins-ci.org/display/JENKINS/ChromeDriver+plugin)
* [ShiningPanda (Python Support)](https://wiki.jenkins-ci.org/display/JENKINS/ShiningPanda+Plugin)

#### Running the tests using Jenkins:
Use the jenkins-selenium.sh file to run the tests on Jenkins
