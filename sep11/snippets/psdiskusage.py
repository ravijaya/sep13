import psutil
from pprint import pprint as pp

for partition in psutil.disk_partitions():
    print(partition.mountpoint)
    usage = psutil.disk_usage(partition.mountpoint)
    print('\ttotal :', usage.total)
    print('\tused :', usage.used)
    print('\tfree :', usage.free)
    print()

# pp(psutil.disk_usage('/home'))