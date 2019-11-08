import pytest

@pytest.yield_fixture()
def setup():
    print("opening URL to Login")
    yield
    print("closing browser after Login")

def test_LoginByemail(setup):
    print("this is Login by email")



def test_LoginByfacebook(setup):
    print("this is Login by facebook")