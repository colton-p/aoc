
line = ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"

from util import *


def evolve(line):
  s = ''
  line = '.' + line + '.'
  for ix in range(1, len(line)-1):
    t = line[ix-1:ix+2]
    if t in ['^..', '..^', '.^^', '^^.']:
      s += '^'
    else:
      s += '.'
  return s

def generator(state):
  while True:
    state = evolve(state)
    yield state

g = generator(line)

s = line
c = 0
for i in range(400000):
  c += (sum(1 for c in s if c == '.'))
  s = next(g)
  print(s)

print(c)


