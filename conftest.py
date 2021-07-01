import os

import pytest


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