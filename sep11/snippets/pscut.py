from optparse import OptionParser

parser = OptionParser()

parser.add_option('-f', '--field', action='store', help='field number')
parser.add_option('-d', '--delimiter', action='store', default=' ', help='delimiter')

(options, args) = parser.parse_args()
print(options.f)
print(options.delimiter)
print(args)
