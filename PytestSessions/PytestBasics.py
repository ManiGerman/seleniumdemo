#GROUPING or MARKING
import pytest

@pytest.mark.Child
def test_name():
       print("mani")
@pytest.mark.Child
def test_name1():
    print("JAYA")
@pytest.mark.Child
def test_name2():
    print("NILA")

def test_name3():
    print("BOY")
