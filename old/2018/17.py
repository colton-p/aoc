#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 17'
print '------'

rows = input_rows('17', test=False)

print 'row count:', len(rows)
print '------'

G = defaultdict(lambda: '.')

for row in rows:

  if row[0] == 'x':
    (x,y0,y1) = extract_numbers(row)

    for y in range(y0, y1+1):
      G[(x,y)] = '#'
  elif row[0] == 'y':
    (y,x0,x1) = extract_numbers(row)

    for x in range(x0, x1+1):
      G[(x,y)] = '#'
  else:
    assert False, row

def open(x,y):
  return G[(x,y)] in ['.', '|']



MIN_Y = min([y for (x,y) in G.keys()])
MAX_Y = max([y for (x,y) in G.keys()])

print MIN_Y, MAX_Y

def drip(x,y):

    if y > MAX_Y:
      return

    #print x, y, MAX_Y

    # look down
    while open(x,y+1):
      (x,y) = (x, y+1)
      if y > MAX_Y:
        break
      G[(x,y)] = '|'

    d = 1
    L = set()
    fill = '~'

    # look left
    while True:
      if y+1 > MAX_Y:
        break
      if open(x-d,y+1):
        # falls down
        drip(x-d, y)
        fill = '|'
        d += 1
        break
      if not open(x-d, y):
        # stop
        break

      d += 1

    e = 0
    while True:
      if y+1 > MAX_Y:
        break
      if open(x+e,y+1):
        # falls down
        drip(x+e, y)
        fill = '|'
        e+=1
        break
      if not open(x+e, y):
        # stop
        break
      elif y+1 > MAX_Y:
        break
      e += 1

    for xx in range(x-d+1, x+e ):
      G[(xx,y)] = fill



    #elif open(x-1, y):
    #  (x,y) = (x-1, y)
    #  G[(x,y)] = '|'
    #else:
    #  G[(x,y)] = '~'
    #  return

for i in range(1000):
  drip(500, 0)
  #print 'xxxx', i, len([((x,y),v) for ((x,y), v) in G.iteritems() if MIN_Y <= y and y <= MAX_Y and v in ['~', '|']])
  print 'xxxx', i, len([((x,y),v) for ((x,y), v) in G.iteritems() if MIN_Y <= y and y <= MAX_Y and v in ['~']])

