import psutil
from pprint import pprint as pp

pp(psutil.disk_io_counters(perdisk=True))