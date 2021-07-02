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
def load_login_data():
    return {
        "email": os.environ.get('HOTJAR_ACCOUNT_EMAIL'),
        "password": os.environ.get('HOTJAR_ACCOUNT_PASSWORD'),
        "remember": True
    }