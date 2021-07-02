import pytest

from .utils import (BASE_URL)
from .utils import get_webdriver


@pytest.mark.signup
def test_signup(load_signup_data):
    """This will serve as the entry point to test the hotjar
       signup process

    Args:
        load_login_data (Dict): username and password to test login
    """
    browser = get_webdriver('chrome')
    browser.get(BASE_URL)
    
    # Lets make sure we didn't get a redirect to a different site
    assert browser.current_url == BASE_URL