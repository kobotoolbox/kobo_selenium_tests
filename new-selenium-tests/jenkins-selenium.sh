#!/bin/bash
set -e

# Run Selenium tests against a KoBo Toolbox server of your choice.
# Example: DOCKER_SELENIUM_SERVER='True' jenkins-selenium.sh

SCRIPT_DIR="$(dirname "$(readlink --canonicalize "${0}")")"
echo "Absolute directory path of this script is \`${SCRIPT_DIR}/\`."

if [[ "${DOCKER_SELENIUM_SERVER,,}" == 'true' ]]; then
    echo 'Starting Dockerized Selenium "standalone server".'
    selenium_container_id="$(docker run --rm --detach --publish-all selenium/standalone-chrome)"

    trap "echo 'Removing Selenium server container.'; docker rm --force --volumes ${selenium_container_id}" EXIT
    echo 'Automatic Selenium server container cleanup configured.'

    selenium_server_port="$(docker inspect --format='{{ (index (index .NetworkSettings.Ports "4444/tcp") 0).HostPort }}' ${selenium_container_id})"
    echo "Selenium server container port \`4444\` mapped to host port \`${selenium_server_port}\`"
    export SELENIUM_REMOTE_WEBDRIVER_ROOT="http://127.0.0.1:${selenium_server_port}"

    cd "${SCRIPT_DIR}"
    echo 'Installing Python dependencies.'
    pip install --requirement requirements.txt

    until grep --quiet 'Selenium Server is up and running' <<< "$(docker logs ${selenium_container_id})"; do
        echo 'sleepy'
        sleep 0.5
    done
    echo 'Selenium server ready.'

    echo 'Running tests via Selenium server.'
    python selenium_test_suite.py
    echo 'Tests complete.'
else
    #Environment variables:
    KOBO_USERNAME="<USERNAME URL GOES HERE>" && export KOBO_USERNAME
    KOBO_PASSWORD="<PASSWORD GOES HERE>" && export KOBO_PASSWORD
    KOBOFORM_URL="<KOBO FORM URL GOES HERE>" && export KOBOFORM_URL
    SELENIUM_BROWSER_VISIBLITY = 0 && export SELENIUM_BROWSER_VISIBLITY
    KOBO_SELENIUM_TESTS="<TESTS LOCATION GOES HERE>"

    cd "${KOBO_SELENIUM_TESTS}"
    pip install -r requirements.txt
    python selenium_test_suite.py
fi
