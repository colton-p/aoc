

from collections import deque
#x = list('decab')
x = list('baecdfgh')
x = list('fbgdceah')
#x = list('abcdefgh')

REV = True

import re

def swap_pos(r, a, b):
  ia = int(a)
  ib = int(b)
  x[ia], x[ib] = x[ib], x[ia]

def swap_letter(r, a, b):
  ia = x.index(a)
  ib = x.index(b)
  x[ia], x[ib] = x[ib], x[ia]

def rotate(r, d, n):
  global x
  xx = deque(x)
  r = -1 if r else 1
  if d == "right":
    xx.rotate(int(n)*r)
  elif d == "left":
    xx.rotate(-int(n)*r)
  else:
    assert False, d
  x = list(xx)


def rotate_l(r, a):
  global x

  if r:
    xx = deque(x)
    ib = x.index(a)
    """
    if (ib > 0):
      ia = (3*(ib-1)) % 5
      xx.rotate( -1* (ia+1))
    else:
      ia = (3*ib -1) % 5
      print ia
      xx.rotate( -1 * (ia+2))
    """
    dd = {
      1: 1,
      3: 2,
      5: 3,
      7: 4,
      2: 6,
      4: 7,
      6: 8,
      0: 9,
    }
    xx.rotate(-dd[ib])
    x = list(xx)

  else: 
    ia = x.index(a)
    xx = deque(x)

    xx.rotate( (ia+1) )
    if ia >=4:
      xx.rotate(1)
    x = list(xx)

def reverse(r, a, b):
  ia = int(a)
  ib = int(b)
  l = x[ia:ib+1]
  l.reverse()
  x[ia:ib+1] = l

def move(r, a, b):
  if r:
    ia, ib = int(b), int(a)
  else:
    ia, ib = int(a), int(b)
  e = x.pop(ia)
  x.insert(ib, e)
  assert x.index(e) == ib

L = [
  ("swap position (\d+) with position (\d+)",    swap_pos),
  ("swap letter ([a-z]) with letter ([a-z])",    swap_letter),
  ("rotate (left|right) (\d+) steps?",           rotate),
  ("rotate based on position of letter ([a-z])", rotate_l),
  ("reverse positions (\d+) through (\d+)",      reverse),
  ("move position (\d+) to position (\d+)",      move),
]


def rule(line):
  for (regex, func) in L:
    match = re.match(regex, line.strip())
    if match:
      func(REV, *match.groups())
      return
  assert False, line


rules = [line.strip() for line in open('21.in', 'r')]
if REV:
  rules.reverse()
for line in rules:
  rule(line)
  print ''.join(x)
