#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 16

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def spin(L, n):
  return L[-n:] + L[:-n]

def ex(L, a, b):
  L[a], L[b] = L[b], L[a]
  return L

def partner(L, a, b):
  ia = L.index(a)
  ib = L.index(b)
  L[ia], L[ib] = L[ib], L[ia]
  return L

def part1(rows, iobj):

  L = list('abcdefghijklmnop')
  for row in rows[0].split(','):
    if row[0] == 's':
      L = spin(L, int(row[1:]))
    elif row[0] == 'x':
      (a,b) = row[1:].split('/')
      L = ex(L, int(a), int(b))
    elif row[0] == 'p':
      L = partner(L, row[1], row[3])
  
  return ''.join(L)


def dance(L):
  ops = rows[0].split(',')

  L = list(L)
  for row in ops:
    if row[0] == 's':
      L = spin(L, int(row[1:]))
    elif row[0] == 'x':
      (a,b) = row[1:].split('/')
      L = ex(L, int(a), int(b))
    elif row[0] == 'p':
      L = partner(L, row[1], row[3])
      
  return ''.join(L)
      


def part2(rows, iobj):

  info = detect_cycle('abcdefghijklmnop', dance)

  return predict_cycle(info, 1_000_000_000)



print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
