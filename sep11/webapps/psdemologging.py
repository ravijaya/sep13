"""demo for the logging"""

import logging

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt_str, filename='access.log')

for item in range(1, 10):
    logging.debug(f'messages : {item}')
# logging.info('confirmation notes')
# logging.warning('warning info')
# logging.error('an error info')
# logging.critical('panic error')