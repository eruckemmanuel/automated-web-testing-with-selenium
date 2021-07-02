from uuid import uuid4

from selenium import webdriver

BASE_URL = "https://hotjar.com"
LOGIN_URL = "https://insights.hotjar.com/login"
SIGNUP_URL = "https://insights.hotjar.com/register"
DEFAULT_WAIT_TIME = 10

SELENIUM_WEBDRIVERS = {
    "chrome": {
        "func": webdriver.Chrome,
        "driver_path": "./drivers/chromedriver"
    },
    "firefox": {
        "func": webdriver.Firefox,
        "driver_path": "./drivers/geckodriver"
    }
}

ELEMENT_SELECTORS = {
    "login_btn": {
        "xpath": "",
        "css": ".nav__link--alt-two",
    },
    "signup_btn": {
        "xpath": "",
        "css": ".nav__link--alt-one"
    },
    "submit_log": {
        "css": "#submit"
    }
}


def get_webdriver(browser):
    """This function will return an instance of selenium webdriver 
       object, based on the browser type requested

    Args:
        browser (String): identifier string for browser type
    """

    driver = SELENIUM_WEBDRIVERS.get(browser)

    return driver.get('func')(driver.get('driver_path'))


def assert_current_url(browser, expected_url):
    """This function will assert that the browser current_url is
        equall to the expected url

    Args:
        browser (selenium.webdriver): An instance of the selenium.webdriver object
        expected_url (String): The URL expected to match current url
    """
    assert browser.current_url == expected_url, \
        "{} does not match the current browser url".format(expected_url)
        


def take_screenshot(browser, file_path=None):
    """This function will take a screenshot of the current browser object and save
        in a provided or generated path.

    Args:
        browser (selenium.webdriver): Selenium webdriver instance
        file_path (String, optional): Provided path to save screenshot. Defaults to None.

    Returns:
        String: Resulting path of the save Screenshot
    """
    if not file_path:
        file_path = "screenshots/{}.png".format(uuid4())
        
    browser.get_screenshot_as_file(file_path)
    return file_path
