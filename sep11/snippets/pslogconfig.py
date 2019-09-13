import logging

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
fmt = logging.Formatter(fmt_str)  # what to log?

sh = logging.StreamHandler()  # console  where to log
fh = logging.FileHandler('secure.log')
sh.setFormatter(fmt)
fh.setFormatter(fmt)

logger = logging.getLogger('danske')
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(sh)
