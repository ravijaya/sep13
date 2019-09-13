import psutil
from optparse import OptionParser
from json import dump
"""http://collabedit.com/sypde"""
parser = OptionParser()
parser.add_option('-f', '--format', default='json', action='store')

options, args = parser.parse_args()

if options.format != 'json':
    raise Exception('unsupported format: {}'.format(options.format))

data_set = {process.pid: process.as_dict() for process in psutil.process_iter()}  # dict comprehension

# pp(data_set)

target_file = args[0]

with open(target_file, 'w') as fw:
    dump(data_set, fw, indent=2)
