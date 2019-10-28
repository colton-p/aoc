#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 14'
print '------'

rows = input_rows('14', test=False)

print 'row count:', len(rows)
print '------'

L = collections.deque([3,7])

x = 0
y = 1

N = 9#int(rows[0])#18
TGT = map(int, '170641')
ix = 0
while True:
  if ix % 100000 == 0:
    print ix
  ix +=1
  s = (L[x]) + (L[y])

  L.extend([int(digit) for digit in str(s)])

  x += (1 + int(L[x]))
  x %= len(L)
  y += (1 + int(L[y]))
  y %= len(L)

  #ss = ''.join(map(str,L[ix-100:]))
  if len(L) > 6:
    if [L[-6], L[-5], L[-4], L[-3], L[-2], L[-1]] == TGT:
      print len(L)-6
      exit()

#print x
#print y
#print ''.join(map(str,L[N:N + 10]))
