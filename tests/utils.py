from uuid import uuid4
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_ERROR_MESSAGE = "Invalid"
DEFAULT_WAIT_TIME = 20

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

NAMED_PAGES = {
    "login": {
        "dest": "https://insights.hotjar.com/login",
    },
    "signup": {
        "dest": "https://insights.hotjar.com/register",
        "is_subset": True
    },
    "home": {
        "dest": "https://www.hotjar.com/"
    },
    "dashboard": {
        "dest": "https://insights.hotjar.com/sites",
        "is_subset": True
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
    },
    "login_error_alert": {
        "xpath": "",
        "css": "#password + div"
    },
    "dashboard_sidebar": {
        "xpath": "",
        "css": "#sidebar"
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
        equal to the expected url

    Args:
        browser (selenium.webdriver): An instance of the selenium.webdriver object
        expected_url (String): The URL expected to match current url
    """
    assert browser.current_url == expected_url, \
        "{} does not match the current browser url {}".format(expected_url,
                                                              browser.current_url)


def assert_current_url_subset(browser, subset_url):
    """This function will assert that the subset_url is a subset of
         the browser current_url

    Args:
        browser (selenium.webdriver): An instance of the selenium.webdriver object
        subset_url (String): The URL expected to match current url
    """
    assert subset_url in browser.current_url, \
        "{} is not part of current browser url {}".format(subset_url,
                                                          browser.current_url)


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

    page = NAMED_PAGES.get(name)

    try:
        if page.get('is_subset'):
            assert_current_url_subset(browser, page.get('dest'))
        else:
            assert_current_url(browser, page.get('dest'))
    except AssertionError as e:
        logger.error("{} - Taking screenshot".format(e))
        take_screenshot(browser, 'screenshots/{}.png'.format(name))

        assert False


def check_visibility_of_element(browser, selector, timeout=DEFAULT_WAIT_TIME):
    """This function will check the visibility of a DOM element and returns the element
        or None if the element is not visible after a duration of timeout.

    Args:
        browser (selenium.webdriver): Instance of webdriver
        selector (String): CSS selector of element
        timeout (Int): timeout for selenium explicit wait

    Returns:
        DOM/None: 
    """
    element = None
    try:
        element = WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutError as e:
        logger.error("{} - Unable to locate visible element {}".format(e, selector))

    return element


def check_presence_of_element(browser, selector, timeout=DEFAULT_WAIT_TIME):
    """This function will check the presence of a DOM element and returns the element
        or None if the element is not found after a duration of timeout. 

    Args:
        browser (selenium.webdriver): Instance of webdriver
        selector (String): CSS selector of element
        timeout (Int): timeout for selenium explicit wait

    Returns:
        DOM/None: Either the element or a none
    """
    element = None
    try:
        element = WebDriverWait(browser, DEFAULT_WAIT_TIME).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutError as e:
        logger.error("{} - Unable to locate element {}".format(e, selector))

    return element
