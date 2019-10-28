from collections import defaultdict
import re


def parse(line):
  m = re.search('bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', line)
  if m:
    src = int(m.group(1))
    dst_low = int(m.group(3))
    dst_high = int(m.group(5))
    if m.group(2) == 'output':
      dst_low = 'o%d' % dst_low
    if m.group(4) == 'output':
      dst_high = 'o%d' % dst_high

    give(src, dst_low, dst_high)
    return

  m = re.search('value (\d+) goes to bot (\d+)', line)
  if m:
    bot = int(m.group(2))
    val = int(m.group(1))
    value(val, bot)
    return

  assert False, line

V = defaultdict(list)

B = defaultdict(list)

def get(bot):

  B[bot] =  [x if type(x) == int else x() for x in B[bot]]
  return B[bot]

def value(val, bot):
  B[bot] += [val]


def give(src, dst_low, dst_high):
  assert src != dst_low
  assert src != dst_high
  B[dst_low] += [lambda : min(get(src))]
  B[dst_high] += [lambda : max(get(src))]


#give(2,1, 0)
#value(3,1)
#give(1,'o1',0)
#give(0, 'o2','o0')
#value(5, 2)
#value(2,2)

for line in open('10.in', 'r'):
  parse(line)


for k in B:
  v = get(k)
  if tuple(sorted(v)) == (17,61):
    print k, get(k)


print get('o0')
print get('o1')
print get('o2')
print get('o0')[0] * get('o1')[0] * get('o2')[0]




