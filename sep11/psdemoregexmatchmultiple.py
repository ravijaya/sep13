"""to match multiple"""

import re

s = 'the python and the python perl scripting'
pattern = 'P.+?N'  # non-greedy match

print(re.finditer(pattern, s, re.I))
print()

for m in re.finditer(pattern, s, re.I):
    print(m.group())
    print(m.span())
    print()
