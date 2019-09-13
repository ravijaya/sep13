import logging

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'

logging.basicConfig(level=logging.DEBUG, format=fmt_str, filename='error.log')

logging.debug('debug messages')
logging.info('confirmation notes')
logging.warning('warnings messages')
logging.error('error informations')
logging.critical('panic error')