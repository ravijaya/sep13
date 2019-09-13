"""user adding users"""

from subprocess import check_call
import os
import sys
from csv import reader
"""http://collabedit.com/sypde"""

if os.getuid() != 0:
    print('{} must be root to run it'.format(sys.argv[0]), file=sys.stderr)
    exit(1)


def delete_user(user_name):
    check_call(['userdel', '-r', user_name])
    print('successfully deleted  the user {}'.format(user_name))


def parse_csv(user_file):
    try:
        for row in reader(open(user_file), delimiter=':'):
            user_name = row[0]
            delete_user(user_name)
    except(FileNotFoundError, IOError) as err:
        print(err)


if __name__ == '__main__':
    parse_csv('userdelist.csv')
