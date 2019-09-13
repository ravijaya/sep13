import re


s = '17/May/2015:10:05:03 GET /presentations/logstash-monitorama-2013/images/kibana-search. 19/June/2017:12:02:03'


pattern = """(?P<date>\d{2}/\D+/\d{4})  # date
                :
                (?P<time>\d{2}:\d{2}:\d{2})  # time
                """

for m in re.finditer(pattern, s, re.VERBOSE):

    print(m.group())
    print(m.group('date'))
    print(m.group('time'))
    print(m.groupdict())
    print()