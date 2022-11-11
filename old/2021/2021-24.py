from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 24

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  pc = 0


  
  INPUT = [1 for i in range(14)]

  def chk(rows, input, zz=0):
    def rhs(val):
      if val in R:
        return R[val]
      return int(val)
    R = {'w': 0, 'x':0 ,'y':0,'z':zz}
    assert rows[0] == 'inp w', rows
    for row in rows:
      if row.startswith('inp'):
        tgt = row.split(' ')[1]
        if not input:
          break
        R[tgt] = input.pop(0)
        continue
    
      (oper, tgt, val) = row.split(' ')
      if oper == 'add':
        R[tgt] = R[tgt] + rhs(val)
      if oper == 'mul':
        R[tgt] = R[tgt] * rhs(val)

      if oper == 'div':
        R[tgt] = R[tgt] // rhs(val)

      if oper == 'mod':
        R[tgt] = R[tgt] % rhs(val)

      if oper == 'eql':
        #if row == 'eql x w' and (R[tgt] ==rhs(val)):
        #  print(row, R[tgt], R[val])
        R[tgt] = int(R[tgt] == rhs(val))

      #print('...', row, R)

    return R['z'] == 0, R
  
  def run_block(start, nblocks, zs):
    C = defaultdict(set)
    for z0 in zs:
      for i in itertools.product(range(1, 10), repeat=nblocks):
        rslt, rr = chk(rows[start*18:18*(start+nblocks)], list(i), z0)
        C[rr['z']].add((i, z0))
    return C
  

  Cs = [{0: (set(), 0)}]
  offset = 0
  for nblocks in [1 for i in range(14)]:
    C = run_block(offset, nblocks, sorted(list(Cs[-1].keys()))[:40000])
    print(offset, nblocks, len(C), min(C), max(C))
    offset += nblocks
    Cs += [C]

  def recon(ccc, tgt):
    #print('rr', len(ccc), tgt)
    C = ccc[-1]
    parents = C[tgt]
    #print(len(parents))
    for (pr, tgt) in parents:
      #print(pr, tgt)
      #print(recon(ccc[:-1], tgt))
      if len(ccc) == 1:
        yield pr
      else:
        for x in recon(ccc[:-1], tgt):
          yield x + pr
    return 'hi'

    for C in reversed(Cs[1:]):
      parents = C[tgt]
  
  qqq = tuple(9 for i in range(14))
  for x in recon(Cs[1:], 0):
    if x < qqq:
      qqq = x
    # print('-->', x, chk(rows, list(x), 0))

  return ''.join(map(str, qqq))
  rslt = []
  tgt = 0
  for C in reversed(Cs[1:]):
    parents = C[tgt]
    best = max(parents, key=lambda x: x[0])
    print(best, len(parents))
    rslt = [best[0][0]] + rslt
    tgt = best[1]

  print(chk(rows, rslt, 0))

  return rslt

  for i in itertools.product(range(1, 10), repeat=2):
    rslt, rr = chk(rows[:18*5], list(i), 0)
    print(i, rr)
    C[rr['z']] += 1
  print(len(C))

  print((run_block(0, 2, [0])))

  return
  C1 = Counter()
  for z0 in C:
    for i in itertools.product(range(1, 10), repeat=1):
      rslt, rr = chk(rows[18*4:18*5], list(i), z0)
      print(i, rr)
      C1[rr['z']] += 1
  print(len(C1))

  return

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
