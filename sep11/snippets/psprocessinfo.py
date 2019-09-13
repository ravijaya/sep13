import psutil
from pprint import pprint as pp
from os import kill

# pp(psutil.pids())
print()

for process in psutil.process_iter(attrs=['pid', 'name', 'username', ]):
    if 'python' in process.name():
        if process.cpu_percent(interval=.3) >= 90:
            pid = process.pid
            print(pid)
            print(process.info, process.cpu_percent(interval=1))
            kill(pid, 9)
