import logging

import pytest

from .utils import (NAME_PAGES, ELEMENT_SELECTORS, DEFAULT_WAIT_TIME)
from .utils import (get_webdriver, assert_current_url, 
                    take_screenshot, open_named_page)

logger = logging.getLogger(__name__)


def enter_login_details(browser, details):
    """Fill login form with user credentials

    Args:
        browser (selenium.webdriver): Selenium webdriver instance
        details (Dict): Dictionary of user credentials
    """
    browser.find_element_by_id('email').send_keys(details.get('email'))
    browser.find_element_by_id('password').send_keys(details.get('password'))
    if details.get('remember'):
        browser.find_element_by_id('remember').click()

@pytest.mark.login
def test_login(load_login_data):
    """This will serve as the entry point to test the hotjar
       login process

    Args:
        load_login_data (Dict): username and password to test login
    """
    browser = get_webdriver('chrome')
    browser.implicit_wait(DEFAULT_WAIT_TIME)
    home_page = NAME_PAGES.get('home').get('dest')
    browser.get(home_page)

    # Lets make sure we didn't get a redirect to a different site
    try:
        assert_current_url(browser, home_page)
    except AssertionError as e:
        logger.error("{} - Taking screeenshot".format(e))

        file_path = 'screenshots/wrong-address/{}.png'.format(home_page.replace('https://', ""))
        take_screenshot(file_path)

        assert False

    # Go to login page
    open_named_page(browser, "login")
    
    # Fill the login form
    enter_login_details(browser, load_login_data)
    
    # Submit login
    submit_login_btn = ELEMENT_SELECTORS.get('submit_login')
    browser.find_element_by_css_selector(submit_login_btn).click()