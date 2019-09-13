import psutil
from pprint import  pprint as pp

print(psutil.sensors_battery())
print()
print(psutil.sensors_fans())
print()
pp(psutil.sensors_temperatures())