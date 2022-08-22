


import pytest
'''
- configtest file is name should be same as it is "conftest"
- that should be available to all the test files in pytest
'''

@pytest.fixture()
def GlobalFixture():
    print("I am from global fixture")
