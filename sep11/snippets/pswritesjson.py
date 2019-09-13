import pyexcel
from json import dump, load
from pprint import pprint as pp
"""http://collabedit.com/ssfen"""




def spreadsheet2json(spreadsheet_file, json_file):
    sheet = pyexcel.get_sheet(file_name=spreadsheet_file)
    keys = ['host', 'port', 'user', 'pwd']

    content = [dict(zip(keys, row)) for row in sheet]
    content = {'ssh-config': content}
    dump(content, open(json_file, 'w'), indent=2)


def read_json(json_file):
    content = load(open(json_file))
    pp(content)


if __name__ == '__main__':
    spreadsheet2json('hosts.xlsx', 'hosts.json')
    read_json('hosts.json')


# pip install pyexcel pyexcel-xlsx