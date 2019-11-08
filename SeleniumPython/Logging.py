import logging


# logging.debug("this is a debug message")
# logging.info("this is a info message")
# logging.warning("this is a warning message")
# logging.error("this is a error message")
# logging.critical("this is a critical message")


#Send logging information to log file
#logging.basicConfig(filename='test.log')  #Same location
#logging.basicConfig(filename='D://SeleniumPython//dummyfiles//test.log')  #Custom location
#logging.basicConfig(filename='D://SeleniumPython//dummyfiles//test.log',
#                    level=logging.DEBUG)  #Adding Level

#
# logging.basicConfig(filename='D://SeleniumPython//dummyfiles//test.log',
#                     format='%(asctime)s :%(levelname)s:  %(message)s:',
#                     level=logging.DEBUG)  #Adding TimeStamp

logging.basicConfig(filename='D://SeleniumPython//dummyfiles//test.log',
                    format='%(asctime)s :%(levelname)s:  %(message)s:',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)  #Changing DateFormat


logging.debug("this is a debug message")
logging.info("this is a info message")
logging.warning("this is a warning message")
logging.error("this is a error message")
logging.critical("this is a crirical message")