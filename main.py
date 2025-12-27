import logging

logging.basicConfig(level=logging.DEBUG, 
                    filename='app.log', filemode='w',
                    format='%(process)d-%(levelname)s-%(message)s-%(asctime)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

a, b = 5, 0
try:
    c = a/b
except Exception as e:
    # logging.error("Expection occurred", exc_info=True)
    logging.exception("Expection occurred")

logger = logging.getLogger('test_logger')
logger.warning('This is Warning !')