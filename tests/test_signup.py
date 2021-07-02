import logging

import pytest

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
    browser.find_element_by_id('password').send_keys(details.get('password'))
    browser.find_element_by_id('terms').click()
    


@pytest.mark.signup
def test_signup(load_signup_data):
    """This will serve as the entry point to test the hotjar
       signup process

    Args:
        load_login_data (Dict): username and password to test login
    """
    browser = get_webdriver('chrome')
    browser.implicitly_wait(DEFAULT_WAIT_TIME)
    
    home_page = NAMED_PAGES.get('home').get('dest')
    browser.get(home_page)

    # Lets make sure we didn't get a redirect to a different site
    try:
        assert_current_url(browser, home_page)
    except AssertionError as e:
        logger.error("{} - Taking screeenshot".format(e))

        file_path = 'screenshots/{}.png'.format(home_page.replace('https://', ""))
        take_screenshot(browser, file_path)

        assert False
    
    # Open the signup page
    open_named_page(browser, "signup")
    
    # Enter Signup details
    fill_signup_form(browser, load_signup_data)
    
    # submit signup
    browser.find_element_by_id('submit').click()
        
    