from collections import Counter
from collections import defaultdict

import re

good_input = "11110010111001001"
size = 35651584
size = 272

def f(a):
  b = str(a)
  b = list(b)
  b.reverse()
  b = ''.join(['1' if bi == '0' else '0' for bi in b])

  return a + '0' + b


def chk1(s):
  for i in range(0, len(s), 2):
    pair = s[i:i+2]
    if pair[0] == pair[1]:
      yield '1'
    else:
      yield '0'

def chk(s):
  while len(s) % 2 == 0:
    s = ''.join(chk1(s))
  return s



s = good_input

while len(s) < size:
  s = f(s)

s = s[:size]
assert len(s) == size

print chk(s)
