import logging
from builtins import Exception

import pytest
from selenium.common.exceptions import NoSuchElementException

from .utils import (NAMED_PAGES, DEFAULT_WAIT_TIME)
from .utils import (get_webdriver, assert_current_url,
                    take_screenshot, open_named_page)

logger = logging.getLogger(__name__)


def fill_signup_form(browser, details):
    """Fill signup data into signup form

    Args:
        browser (selenium.webdriver): Instance of selenium webdriver
        details (Dict): Dictionary object of signup data
    """

    # We first open the signup form to show signup inputs
    browser.find_element_by_id('show-email-fields').click()

    browser.find_element_by_id('name').send_keys(details.get('name'))
    browser.find_element_by_id('email').send_keys(details.get('email'))

    try:
        browser.find_element_by_id('password').send_keys(details.get('password'))
    except NoSuchElementException as e:
        logger.error("{} - Password Element not found".format(e))

    try:
        browser.find_element_by_id('terms').click()
    except Exception as e:
        logger.error("{} - Error checking terms".format(e))


@pytest.mark.signup
def test_signup(load_signup_data):
    """This will serve as the entry point to test the hotjar
       signup process

    Args:
        load_signup_data (Dict): username and password to test signup
    """
    browser = get_webdriver('chrome')
    browser.implicitly_wait(DEFAULT_WAIT_TIME)

    home_page = NAMED_PAGES.get('home').get('dest')
    browser.get(home_page)

    # Lets make sure we didn't get a redirect to a different site
    try:
        assert_current_url(browser, home_page)
    except AssertionError as e:
        logger.error("{} - Taking screenshot".format(e))
        take_screenshot(browser, "screenshots/signup.png")

        assert False

    # Open the signup page
    open_named_page(browser, "signup")

    # Enter Signup details
    fill_signup_form(browser, load_signup_data)

    # submit signup
    browser.find_element_by_id('submit-step-1').click()
