import re
from pprint import pprint as pp
import matplotlib.pyplot as plt
pattern = r"""
(?P<remote_addr>\S+)   # ipaddress
\s+
\S+  # remote logname
\s+
\S+  # remote user
\s+
\[[^\[\]]+\]  # timestamp
\s+
"[^"]+"  # request
\s+ 
(?P<status_code>\d+)  # status code
\s+
(?P<bytes_sent>-|\d+) #bytes sent
\s*
"""
compile = re.compile(pattern, re.VERBOSE)


def plot_pie_chart(list_of_addr, list_of_bytes):
    """plot pie char"""

    plt.pie(list_of_bytes, labels=list_of_addr, startangle=90, autopct='%.1f%%')
    plt.title("Usage By IP Address")
    plt.savefig('bytes_ip_pie.png')
    plt.show()


def plot_bar_chart(list_of_addr, list_of_bytes):
    """plot bar chart"""

    x_pos = range(len(list_of_addr))

    plt.bar(x_pos, list_of_bytes)
    plt.xticks(x_pos, list_of_addr, rotation=90)  # mark label on x-axis
    plt.xlabel('IP Address')
    plt.ylabel('Bytes Sent')

    plt.title("Usage By IP Address")
    plt.savefig('bytes_ip_bar.png')
    plt.show()


def dictify_the_line(line):
    m = compile.search(line)

    if m:
        data = m.groupdict()
        if data['bytes_sent'] == '-':
            data['bytes_sent'] = 0

        return data

    return {'remote_addr': '', 'status_code': 0, 'bytes_sent': 0}


if __name__ == '__main__':
    group_bytes_sent_by_addr = {}

    with open('access.log') as fp:
        for line in fp:
            d = dictify_the_line(line)
            group_bytes_sent_by_addr.setdefault(d['remote_addr'], []).append(int(d['bytes_sent']))

    # pp(group_bytes_sent_by_addr)
    # exit(1)
    summed = [(sum(list_of_bytes), addr) for addr, list_of_bytes in group_bytes_sent_by_addr.items() if
              sum(list_of_bytes)]
    summed = sorted(summed)
    # pp(summed)
    # exit(1)

    bytes_sent = [item[0] for item in summed[-30:]]
    remote_address = [item[1] for item in summed[-30:]]

    # pp(bytes_sent)
    # pp(remote_address)

    # plot_bar_chart(remote_address, bytes_sent)
    plot_pie_chart(remote_address, bytes_sent)
