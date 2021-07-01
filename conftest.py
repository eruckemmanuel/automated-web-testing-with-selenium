import os

import pytest
from dotenv import load_dotenv


load_dotenv()

@pytest.fixture()
def load_signup_data():
    return {
        "name": "Hotjar Tester",
        "email": "eruck@vehseh.com",
        "password": os.environ.get('HOTJAR_PASSWORD')
    }


@pytest.fixture()
def load_login_data():
    return {
        "email": "eruck@vehseh.com",
        "password": os.environ.get('HOTJAR_PASSWORD')
    }