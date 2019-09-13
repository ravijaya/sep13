import re
from fileinput import input, filelineno
from time import time

pattern = ':'
replacement = ','
line_no = 1

for line in input('passwd', inplace=True, backup=f'{time()}.bak'):
    if re.search('^#', line):
        print(line, end='')
        continue

    if line_no <= 10:
        line = re.sub(pattern, replacement, line)

    line_no += 1
    print(line, end='')
