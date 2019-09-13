import psutil
from pprint import pprint as pp

pp(psutil.disk_partitions())
print()
pp(psutil.disk_partitions(all))
print()

pp(psutil.disk_usage('/home'))