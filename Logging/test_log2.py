'''
Logging Types:
- Debug
- Info
- Warning
- Error
- Critical
'''

#default package 
import logging
from BaseLog import getLogger

def test_loggingFun():

     #check logger declared from Baselog file
    log=getLogger()

    log.info("I am from test_log2 using log from BaseLog")



    