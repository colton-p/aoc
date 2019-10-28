import collections
import re

PAIRS = set()

SIZE = dict()
CAP = dict()


def parse(line):
  m = re.search('node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)', line)
  if m:
    x = int(m.group(1))
    y = int(m.group(2))

    CAP[(x,y)] = int(m.group(3))
    SIZE[(x,y)] = int(m.group(4))
  else:
    assert False, line


for line in open('22.in', 'r'):
  parse(line)

def adj(state):
  for i in [-1, 1]:
    a = (state[0] + i, state[1])
    if a in SIZE:
      yield a
    a = (state[0], state[1]+i)
    if a in SIZE:
      yield a

def search(start):
  visited = 0
  to_visit = collections.deque([ start ])
  distance = {}
  distance[start] = SIZE[start]

  while to_visit:
    state = to_visit.popleft()
    depth = distance[state]
    if state != start:
      PAIRS.add(tuple(((start,state))))
      print start, state, depth, CAP[state]

    for s in adj(state):
      if depth + SIZE[s] <= CAP[s]:
        distance[s] = depth + SIZE[s]
        to_visit.append(s)

C = 0
D = {}
E = ''

def pp():
  for y in range(26):
    for x in range(38):
      print D[(x,y)],
    print ''

for y in range(26):
  for x in range(38):
    if (x,y) == (37,0):
      D[(x,y)] = 'G'
    elif SIZE[(x,y)] > 80:
      D[(x,y)] = '#'
    elif SIZE[(x,y)] < 60:
      D[(x,y)] = 'O'
      E = (x,y)
    elif float(SIZE[(x,y)])/CAP[(x,y)] > 0.5:
      D[(x,y)] = '.'

def move(dd):
  global C, D, E
  C += 1
  (x,y) = dd

  a = (E[0], E[1])
  b = (E[0] + x, E[1]+y)
  D[a], D[b] = D[b], D[a]
  E = b
  assert D[b] != '#'
  assert b[0] >= 0
  assert b[1] >= 0

pp()
for i in range(17):
  move( (-1,0))
for i in range(22):
  move( (0,-1))
for i in range(37):
  move( (1,0))

for i in range(36):
  move(( 0, 1))
  move((-1, 0))
  move((-1, 0))
  move(( 0,-1))
  move(( 1, 0))
print ''
pp()
print C

