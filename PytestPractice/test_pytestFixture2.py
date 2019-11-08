import pytest

@pytest.yield_fixture()
def setup():
    print("once before every method")
    yield
    print("once after every method")


def testmethod1(setup):
    print("this is test method1")

def testmethod2(setup):
    print("this is test method2")

def testmethod3():
    print("this is test method3")