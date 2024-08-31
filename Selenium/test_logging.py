# here we will learn how to log the results in a log file like at what time the script was executed, and what errors/info were triggered incase the testexecution fails

import logging
# we need to import the logging package inorder to use the logger
def test_loggingdemo():
    logger = logging.getLogger(__name__)
# here we are creation a object where the logging package can be used
# also we need to pass the __name__ argument so that the logger knows which file we are currently logging
# now we need to create a log file where the logging data can be stored
    logging_data = logging.FileHandler('logfile.log')
# the Filehandler method is used to specify where the log data need to be stored into with the syntax [logging.FileHandler('<filename.log>')]
# now we just need to pass the file location into the object we created
    logger.addHandler(logging_data)
# now we need to specify the format on how the log should be generated soo we use the method [logging.Formatter]
# as we also need to use this format we need to store it in a object
    Format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
# here we are enclosing the keywords in % and s
# the % will execute the keywords during run time and the 's' is used to convert all the keywords we as passing as strings
# asctime = is a inbuilt keyword that is used to return the current time of the execution in format Y/M/D H/M/S
# levelname = is a inbuilt keyword that is used to return the type of log(error/info/warning/critical)
# name = this prints the testcase name which the log generates
# message = this prints the message that we pass to each of the log (the message we are passing for the debug/info/warning/error etc)
# if we need to display logs skipping the debug and info we can do it by using this method, here this will display logs for warning, error and critical

# we now need to connect this format that we created into the file location that we created
    logging_data.setFormatter(Format)
    logger.setLevel(logging.DEBUG)
# Note : the above steps is the correct herarchy that we defined for the logger debug>info>warning>error>critical
    logger.debug("This logs the data from the debug section of the testcase")
    logger.info("This logs the data of all the info of a particular testcase")
    logger.warning("All warnings will be stored here")
    logger.error("All errors will be stored here")
    logger.critical("Any critical defects which halt the progress of the testrun will be stored here")
