import csv
from time import time



def write_attempts(attempts, fname):
    with open(fname, 'w') as fpout:
        writer = csv.writer(fpout)
        writer.writerow(['Username', 'Timestamp', 'Success'])
        for attempt in attempts:
            writer.writerow(attempt)


if __name__ == '__main__':
    print(('ravi', time(), False))