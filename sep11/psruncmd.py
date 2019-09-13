"""demo for the bytes"""

from subprocess import check_output
from sys import platform

if platform in ['linux', 'darwin']:
    cmd = ['ifconfig']
else:
    cmd = ['ipconfig']

output = check_output(cmd)
print(output.decode())
