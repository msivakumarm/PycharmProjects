import pytest

@pytest.yield_fixture()
def setup():
    print("opening URL to Signup")
    yield
    print("closing browser after Signup")

def test_SignupByemail(setup):
    print("this is Signup by email")



def test_SignupByfacebook(setup):
    print("this is Signup by facebook")