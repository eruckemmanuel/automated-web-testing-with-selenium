import os

import pytest
from dotenv import load_dotenv


load_dotenv()

@pytest.fixture()
def load_signup_data():
    return {
        "name": os.environ.get('HOTJAR_ACCOUNT_NAME'),
        "email": os.environ.get('HOTJAR_ACCOUNT_EMAIL'),
        "password": os.environ.get('HOTJAR_ACCOUNT_PASSWORD')
    }

 
    
@pytest.fixture()
def get_correct_credentials():
    return {
        "email": os.environ.get('HOTJAR_ACCOUNT_EMAIL'),
        "password": os.environ.get('HOTJAR_ACCOUNT_PASSWORD'),
        "remember": False
    }
    

@pytest.fixture()
def get_wrong_credentials():
    """This fixture will add hotjar to the actual password to make it wrong

    Returns:
        Dict: Dictionary of wrong password
    """
    return {
        "email": os.environ.get('HOTJAR_ACCOUNT_EMAIL'),
        "password": "{}hotjar".format(os.environ.get('HOTJAR_ACCOUNT_PASSWORD')),
        "remember": False
    }