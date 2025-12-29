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

logger = logging.getLogger(__name__)
# logger.warning('This is Warning !')
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)

f_handler = logging.FileHandler('app.log')
f_handler.setLevel(logging.WARNING)

c_format = logging.Formatter('%(name)s-%(levelname)s-%(message)s-%(asctime)s') 
c_handler.setFormatter(c_format)
f_handler.setFormatter(c_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)
logger.warning('this is warning')