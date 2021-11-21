from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 24

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def parse_row(row):
  L = []
  while row:
    if row[:2] in ['se', 'sw', 'nw', 'ne']:
      L += [row[:2]]
      row = row[2:]
    elif row[:1] in ['e', 'w']:
      L += [row[:1]]
      row = row[1:]
    else:
      assert False, row
  return L

DD = {
  'e': (1, 0, -1),
  'w': (-1, 0, 1),
  'ne': (1, -1, 0),
  'nw': (0, -1, 1),
  'se': (0, 1, -1),
  'sw': (-1, 1, 0),
}


def follow(path):
  pt = (0, 0, 0)

  for x in path:
    pt = vadd(pt, DD[x])
  return pt

    


def part1(rows, iobj):

  G = defaultdict(lambda: False)

  for row in rows:
    path = parse_row(row)
    pt = follow(path)
    G[pt] = not G[pt]
  
  return sum(G.values())

def nadj(G, pt):
  nb = 0
  for step in DD.values():
    adj = vadd(pt, step)
    if G[adj] == True:
      nb+=1
  return nb

def evolve(G):
  H = defaultdict(lambda: False)
  GG = dict(G)

  for i in range(2):
    for pt in dict(G):
      nb = nadj(G, pt)
      if G[pt] == True:
        if (nb == 0  or nb > 2):
          H[pt] = False
        else:
          H[pt] = True

      if G[pt] == False:
        if (nb == 2):
          H[pt] = True
        else:
          H[pt] = False
  
  return H



def part2(rows, iobj):
  G = defaultdict(lambda: False)

  for row in rows:
    path = parse_row(row)
    pt = follow(path)
    G[pt] = not G[pt]
  
  for i in range(100):
    G = evolve(G)
    print(i, sum(G.values()))

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
