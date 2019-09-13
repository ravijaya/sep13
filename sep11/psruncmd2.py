"""demo for the bytes"""

from subprocess import check_output
from sys import platform
from os import getpid

r"""\u https://pastebin.com/XnPwxRVA"""

print('process id :', getpid())

if platform in ['linux', 'darwin']:
    list_of_commands = [
        ['bash', '-c', 'echo $$; echo $0'],
        ['ls', '-l', '/etc/passwd'],
        ['bash', '-c', 'history']]
else:
    cmd = ['ipconfig']

for cmd in list_of_commands:
    output = check_output(cmd)
    print(output.decode())
    print()
