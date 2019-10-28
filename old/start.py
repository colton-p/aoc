import sys

day = int(sys.argv[1])

out = ''.join([l for l in open('template.py', 'r')]) % (day, day)

with open('%d.py' % day, 'w') as f:
  f.write(out)


