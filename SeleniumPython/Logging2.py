import logging

logging.basicConfig(filename='D://SeleniumPython//dummyfiles//test1.log',
                    format='%(asctime)s :%(levelname)s:  %(message)s:',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

#We will create logger object , based on level will use in projects
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


logger.debug("this is a debug message")
logger.info("this is a info message")
logger.warning("this is a warning message")
logger.error("this is a error message")
logger.critical("this is a crirical message")