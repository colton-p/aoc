from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 13

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
#iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):
  tgt = int(rows[0])

  buses = ints(rows[1])

  for i in range(tgt, tgt + 400):
    for b in buses:
      if i % b == 0:
        return b * (i - tgt)

  return buses

def part2(rows, iobj):

  bb = list(enumerate(rows[1].split(',')))

  bb = [(offset ,int(id)) for (offset, id) in bb if id != 'x'] 

  ak = [id-offset for (offset,id) in bb]
  MM = prod(id for (_, id) in bb)
  Mk = [MM // id for (_,id) in bb]
  Yk = [modinv(Mk[k], bb[k][1]) for k in range(len(bb))]

  x = 0
  for (a, M, y) in zip(ak, Mk, Yk):
    x +=  a*M*y

  return x % MM
  for t in range(0, 999999999999):
    if all((t+offset) % id == 0 for (offset, id) in bb):
      return t


  return bb

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
