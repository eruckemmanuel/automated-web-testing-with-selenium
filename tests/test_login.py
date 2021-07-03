import logging
import pdb

import pytest

from .utils import (NAMED_PAGES, ELEMENT_SELECTORS, DEFAULT_WAIT_TIME, LOGIN_ERROR_MESSAGE, check_visibility_of_element,
                    check_presence_of_element)
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
        try:
            browser.find_element_by_id('remember').click()
        except Exception as e:
            logger.error("{} - Taking screenshot".format(e))
            take_screenshot(browser,
                            "screenshots/{}.png".format(browser.current_url.replace("https://", "")))
            assert False


def perform_login(login_data, fail=False):
    """This will serve as the entry point to test the hotjar
       login process

    Args:
        login_data (Dict): username and password to test login
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

    # Go to login page
    open_named_page(browser, "login")

    # Fill the login form
    enter_login_details(browser, login_data)

    # Submit login
    submit_login_btn = ELEMENT_SELECTORS.get('submit_login').get('css')
    browser.find_element_by_css_selector(submit_login_btn).click()

    if fail:
        # Confirm login error message is displayed
        logger.info("Verifying that login has failed")

        login_error_alert = ELEMENT_SELECTORS.get('login_error_alert').get('css')
        element = check_visibility_of_element(browser, login_error_alert)

        if element:
            logger.info(element.text)
            assert LOGIN_ERROR_MESSAGE in element.text
        else:
            assert False

    else:
        # Confirm that there's a redirect to dashboard
        logger.info('verifying that login was successful')

        dashboard_sidebar = ELEMENT_SELECTORS.get('dashboard_sidebar').get('css')
        element = check_presence_of_element(browser, dashboard_sidebar)

        assert element is not None
        
        take_screenshot(browser, 'screenshots/dashboard.png')        
        assert NAMED_PAGES.get('dashboard').get('dest') in browser.current_url
    
    browser.close()

@pytest.mark.failed_login
def test_failed_login(get_wrong_credentials):
    """Entry point for failed login test

    Args:
        get_wrong_credentials (Dict): Fixture function for wrong user credentials
                                      Dictionary of wrong user credentials
    """
    perform_login(get_wrong_credentials, fail=True)


@pytest.mark.successful_login
def test_successful_login(get_correct_credentials):
    """Entry point for successful login test

    Args:
        get_correct_credentials (Dict): Fixture function for correct user credentials
                                        Returns a Dictinary of correct user credentials
    """
    perform_login(get_correct_credentials)
