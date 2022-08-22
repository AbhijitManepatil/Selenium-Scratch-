'''
Fixture are the pre-requisites to the executing a test cases.
Examaple Fixtures used for:
- setup browser configuration.
- database configuration/instance.
- setting up variable configuration.
- Fixture can be Pre or Post

'''


import pytest


@pytest.fixture() #declair Fixture
def myfixture():
    print("I am from Pre fixture***************")
    yield #TO run post fixture
    print("I am from Post Fixture##############")


def test_fixtureDemo(myfixture):
    print("I am working with fixture")