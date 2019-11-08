import pytest

@pytest.yield_fixture()
def setup():
    print("opening URL to Login")
    yield
    print("closing browser after Login")

def test_loginByemail(setup):
    print("this is login by email")



def test_loginByfacebook(setup):
    print("this is login by facebook")