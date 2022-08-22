'''
To run specific test-case/function,
Tag test-case as of test type example smoke, regression etc.
To do tagging the decorator is defined.
'''

'''
To run smoke(specific) type of test-cases:
> py.test -m smoke -v -s  #smoke is tag name 
# -m : Mark
'''

'''
***************************
# Marks are Custom Marks and Default Marks
# to skip the perticular test
@pytest.mark.skip :decorator
'''
import pytest

#tag func/test-case
@pytest.mark.smoke #tagging test-case as of smoke type
@pytest.mark.skip #Skipping this test case
def test_myfun1():
    '''
    pytest function always start with 'test' keyword
    '''
    print("hi I am Abhijit, from fun1")


def test_myfun2():
    '''
    pytest function always start with 'test' keyword
    '''
    print("hi I am from func2")