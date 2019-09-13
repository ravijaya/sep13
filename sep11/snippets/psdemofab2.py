from fabric import SerialGroup, Connection
from pyexcel import get_sheet
from pprint import pprint as pp


def disk_free(c):
    uname = c.run('uname -s', hide=True)

    if 'Linux' in uname.stdout:
        command = "df -h / | tail -n1 | awk '{print $5}'"
        return c.run(command, hide=True).stdout.strip()

    err = "No idea how to get disk space on {}!".format(uname)

    raise Exception(err)


# hosts = ["{}@{}".format(row[2], row[0]) for row in get_sheet(file_name='hosts.xlsx') if len([col for col in row if col]) > 1]

hosts = []

for row in get_sheet(file_name='hosts.xlsx'):
    row = [col for col in row if col]
    if len(row) == 1:
        continue
    hosts.append("{}@{}".format(row[2], row[0]))

pp(hosts)
print()
print(SerialGroup(*hosts))
print()
for cxn in SerialGroup(*hosts):
    print("{}: {}".format(cxn, disk_free(cxn)))
