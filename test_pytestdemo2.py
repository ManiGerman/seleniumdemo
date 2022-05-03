import pytest
@pytest.yield_fixture()
def setup():
    print("once before every method")
    yield
    print("once After every method")

def testMethod1(setup):
    print("This is test method 1")

def testMethod2(setup):
    print("This is method 2") 