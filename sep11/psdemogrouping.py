import re
"ravi.goglobium@gmail.com"
s = '09 Sep 2019 10:57:41  a sample or a dummy log'

"""https://pastebin.com/raw/N1ZqY7LG"""
# grouping aka baclref.

pattern = r'(\d{2} \D{3} \d{4}) (\d{2}:\d{2}:\d{2})(\s.+)'
pattern = r'(09 Sep 2019 10:57:41)\s+(.+)'
m = re.search(pattern, s)
print(m)
print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))
#print(m.group(3))