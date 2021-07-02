from uuid import uuid4
import logging

from selenium import webdriver


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


NAME_PAGES = {
    "login": {
        "dest": "https://insights.hotjar.com/login",
    },
    "signup": {
        "dest": "https://insights.hotjar.com/register"
    },
    "home": {
        "det": "https://hotjar.com"
    }
}

ELEMENT_SELECTORS = {
    "login": {
        "xpath": "",
        "css": ".nav__link--alt-two",
    },
    "signup": {
        "xpath": "",
        "css": ".nav__link--alt-one"
    },
    "submit_login": {
        "xpath": "",
        "css": "#submit"
    }
}


logger = logging.getLogger(__name__)


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
        file_path = "screenshots/{}.png".format(str(uuid4()))
        
    browser.get_screenshot_as_file(file_path)
    return file_path


def open_named_page(browser, name):
    """Selects a name page button, clicks and 
        asserts that resulting page matches the expected result

    Args:
        browser (selenium.webdriver): Instance of webdriver object
        name (String): name of named page in directory of NAMED_PAGES
    """
    named_page_link = ELEMENT_SELECTORS.get(name).get('css')
    browser.find_element_by_css_selector(named_page_link).click()
    
    page_destination = NAME_PAGES.get(name).get('dest')

    try:
        assert_current_url(browser, page_destination)
    except AssertionError as e:
        logger.error("{} - Taking screenshot".format(e))
        file_path = 'screenshots/wrong-address/{}.png'.format(page_destination.replace('https://', ""))
        take_screenshot(file_path)

        assert False
