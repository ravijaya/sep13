from json import dump
from os import listdir
from os.path import join, getmtime, getsize
from time import ctime, time


def write_json(json_file, *args):
    container = dict()

    for dir_name in args:
        for item in listdir(dir_name):
            abs_path = join(dir_name, item)
            properties = [getsize(abs_path), ctime(getmtime(abs_path))]
            container.setdefault(dir_name, {})[item] = properties

    dump(container, open(str(time())+json_file, 'w'), indent=2)


write_json('tmp.json', '/tmp', '/home/ravijaya', '/home/ravijaya/Downloads')
"""https://pastebin.com/raw/GtD1Xj7X"""