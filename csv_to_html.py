import csv
import sys

if len(sys.argv) < 2:
    print('Usage >> ', sys.argv[0], 'file1 <file2>')
    sys.exit(1)
print('<html><head></head><body><table>')

for i in sys.argv[1:]:
    for line in csv.reader(open(i, 'r')):
        print('<tr>')
        for elm in line:
            print('<td>', str(elm), '</td>')
            print('</td>')
print('</table></body></html>')