import psutil
from pprint import pprint as pp

print(psutil.net_io_counters())
print()
pp(psutil.net_io_counters(pernic=True))
print()
pp(psutil.net_connections())
print()
pp(psutil.net_connections(kind='inet6'))