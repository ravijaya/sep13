import pyexcel
from pprint import pprint as pp
from json import dump

container = {}

group = None
keys = ['host', 'port', 'user', 'pwd']

for row in pyexcel.get_sheet(file_name='hosts.xlsx'):
    row = [item for item in row if item]

    if len(row) == 1:
        group = row[0]
        continue

    container.setdefault(group, []).append(dict(zip(keys, row)))


pp(container)
dump(container, open('group.json', 'w'), indent=2)