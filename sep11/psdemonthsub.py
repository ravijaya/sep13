"""nth sub """
import re
match_counter = 0
# ? :

def nth_replacement(m):
    global match_counter
    match_counter += 1
    return replacement if match_counter in position else m.group()


s = 'nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin'
pattern = ':'
replacement = ','
position = [3, 5]

s2 = re.sub(pattern, nth_replacement, s)
print(s2)
