"""demo for the regex match operation"""

import re
from fileinput import input, filename, filelineno


def grep_me(pattern, *args):
    c = re.compile(pattern, re.I)  # validate's

    for line in input(args):
        if c.search(line):
            # print(f'{filename()}:{filelineno()}:{line}', end='')
            print(line, end='')


pattern = '^$'
pattern = 'b.t'
pattern = 'b[aeiou]t'  # character set
pattern = 'b[^aeiou]t'  # character set
pattern = r'\b[6-9][0-9]{9}\b'
pattern = r'(\D+,\b[0-9]{3}(-| )?[0-9]{3}(-| )?[0-9]{4}\b)|'
pattern += r'(\b[0-9]{3}(-| )?[0-9]{3}(-| )?[0-9]{4}\b\D+)'
#pattern = r'\b\d{3}(-| )?\d{3}(-| )?\d{4}\b'
pattern = r'\b(\D+,(\d{3}(-| )?){2}\d{4})|((\d{3}(-| )?){2}\d{4},\D+)\b'

pattern = r'\b([5-9]\d{2})\b|\b([1-9][0-9]{3}[0-9]*)\b'
pattern = r'\b([5-9]\d{2})\b|\b([1-9][0-9]{2}[0-9]+)\b'
pattern = r'\b([5-9]\d{2})\b|\b([1-9][0-9]{3,})\b'
pattern = r'\b([2-9]\d{2})\b|\b([1-9]\d{3,})\b'
grep_me(pattern, '/etc/passwd')
