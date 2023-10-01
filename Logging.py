import logging

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")



#LOGGING EXCEPTIONS
'''try:
    1 / 0
except ZeroDivisionError as e:
    logging.exception("test")'''





'''x = 2
logging.debug(f"the value of x is {x}") '''#least imp to most imp
'''logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")'''




#CUSTOM LOGS
logger = logging.getLogger(__name__)

handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime) - %(name)s -%(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("test the custom logger")