from optparse import OptionParser

parser = OptionParser()
"""https://pastebin.com/raw/ECm2VEGp"""

parser.add_option('-m', '--mirror', action='store_true', default=False, help='mirroring the file')
parser.add_option('-r', '--reverse', action='store_true', default=False,  help='reversing the file')

(options, args) = parser.parse_args()

content = open(args[0]).readlines()

if options.reverse:
    content.reverse()

if options.mirror:
    content = [line.rstrip()[::-1] + '\n' for line in content]

print(''.join(content), end='')
