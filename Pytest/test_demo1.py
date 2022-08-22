'''
- Pytest file always start with 'test_'
- Method/Fucntion name should start with 'test'
- any code should be wrapped in funtion only.
'''

'''
run test file in pytest,
> py.test -v -s 
# -v : verbose
# -s : command printing values
# 

# with some file to run test
> py.test file_name.py -v -s

# with some selected test-cases/function from any of test files
> py.test -k CreditCard -v -s
# -k : regex pattern, run all specific fun/test-cases containg a 'CreditCard'


'''
###log TEST (later check)'
# from ..Logging.BaseLog import getLogger
from ..Logging.BaseLog import getLogger
import pdb
def test_myfun1():
    '''
    pytest function always start with 'test' keyword
    '''
    # print("hi I am Abhijit, from fun1")

    ##TEST LOG ************** (later check)
    # pdb.set_trace()
    log=getLogger()
    log.critical("I am from BASE CLASS TEST******")


def test_myfun2():
    '''
    pytest function always start with 'test' keyword
    '''
    print("hi I am from func2")