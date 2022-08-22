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


def test_loggingFun():
    #create object
    logger=logging.getLogger(__name__)
    '''
    __name__ : filename
    '''
    #Store log in File
    fileHandler=logging.FileHandler('logfile.log') #file location
    #set format : timeStamp:levelName:FileName:Message
    formater=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(message)s")
    fileHandler.setFormatter(formater) #pass formater to filehandler
    logger.addHandler(fileHandler) #filehandler object


    ##Setlevel
    logger.setLevel(logging.DEBUG) #from this level used for logging above are skipped


    #level 1 :debug
    logger.debug("A debug statement is executed")

    #level 2: info
    logger.info("Imformation statement")

    #level 3: warning
    logger.warning("Something is in warning mode")

    #level 4:error
    logger.error("A Major error has happend")

    #leve 5: Critical
    logger.critical("A Critical Issue")