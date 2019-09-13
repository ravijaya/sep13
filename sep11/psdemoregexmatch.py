import re


s = 'the python and the python perl scripting'
pattern = 'P.+?N'  # non-greedy match
"""https://pastebin.com/raw/LB2YPDdr"""

m = re.search(pattern, s, re.I)

if m:
    print(m)
    print('match string :', m.group())
    #print(m.start())
    #print(m.end())
    print(s[:m.start()])
    print(s[m.end():])
else:
    print('failed to match')
