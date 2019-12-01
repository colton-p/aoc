import sys

day = int(sys.argv[1])
if len(sys.argv) == 3:
  year = int(sys.argv[2])
else:
  year = 2019

out = ''.join([l for l in open('template.py', 'r')])
out = out.replace('<year>', str(year))
out = out.replace('<day>', str(day))


filename = '%d-%d.py' % (year, day)

with open(filename, 'w') as f:
  f.write(out)

