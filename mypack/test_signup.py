import pytest
@pytest.fixture()
def setup():
    print("URL opening to sign up")
    yield
    print("closing the browser after sign up ")

def test_loginbyemail(setup):
    print("This is signup by email test")

def test_loginbyfacebook(setup):
    print("This is signup by facebook test")
