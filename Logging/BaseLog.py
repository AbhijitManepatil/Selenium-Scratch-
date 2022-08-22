'''
Global Logger class
Used dynamically in all over the files/project and test-cases
'''
import logging
import pdb

def getLogger():
    pdb.set_trace()
    '''
    Global debugger used all over the project
    '''
    # Step 1: 
    #Create a loggin object
    print("I am looger base Class **************")
    logger=logging.getLogger(__name__)  #__name__ is file Name

    # Step 2:
    #set file location and object
    fileHandler=logging.FileHandler('logfile.log') #file location

    # Step 3:
    # Set logger format
    formater=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(message)s")

    # Step 4:
    # Set formatter to logger object
    fileHandler.setFormatter(formater)
    logger.addHandler(fileHandler)

    # Step 5:
    #Setlevel
    logger.setLevel(logging.DEBUG)

    return logger