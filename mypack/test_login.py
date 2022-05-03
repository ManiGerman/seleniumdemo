import pytest
@pytest.fixture()
def setup():
    print("URL opening to login")
    yield
    print("closing the browser after login ")

def test_loginByemail(setup):
    print("This is Login by email test")

def test_loginbyfacebook(setup):
    print("This is login by facebook test")
