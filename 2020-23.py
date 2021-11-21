from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 23

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()


class Node():
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None
  
  def __str__(self):
    nv = self.next and self.next.val
    pv = self.prev and self.prev.val
    return f"{self.val} (p={pv} n={nv})"
  
  def chk(self):
    assert self.next.prev == self
    assert self.prev.next == self
  
  def pp(self):
    print(self.val, end=' ')
    self.chk()
    n = self.next
    while n and n != self:
      n.chk()
      print(n.val, end=' ')
      n = n.next
    print('')


NN = 1_000_000
def p(x, n):
  if x <= 0: x+= NN
  return x

def select_dst_val(cur_val, picks):
  dsts = [p(cur_val - 1,NN), p(cur_val - 2,NN), p(cur_val - 3,NN), p(cur_val - 4,NN)]
  return [x for x in dsts if x not in picks][0]     

def move(cur, M):

  # cur -> pick1 -> pick2 -> pick3 -> new_cur -> ... -> dst -> dst2

  # cur -> new_cur -> ... -> dst -> pick1 -> pick2 -> pick3 -> dst2

  pick1 = cur.next
  pick2 = pick1.next
  pick3 = pick2.next
  new_cur = pick3.next

  dst_val = select_dst_val(cur.val, {pick1.val, pick2.val, pick3.val})
  dst = M[dst_val] 
  dst2 = dst.next

  cur.next = new_cur
  new_cur.prev = cur

  dst.next = pick1
  pick1.prev = dst

  pick3.next = dst2
  dst2.prev = pick3

  return new_cur
  

def part1(rows, iobj):
  L = list(rows[0]) +  list(range(10, 1_000_000+1))

  L = [ Node(int(v)) for v in L]
  M = { n.val: n for n in L}

  for (ix, n) in enumerate(L):
    n.next = L[(ix+1) % len(L)]
    n.prev = L[(ix-1) % len(L)]
  
  cur = L[0]

  for i in range(10_000_000):
    if i % 1_000_000 == 0:
      print(i)
    cur = move(cur, M)
  
  print(M[1])
  (a,b) = M[1].next.val, M[1].next.next.val
  print(a)
  print(b)
  return a*b

import cProfile

cProfile.run('part1(rows, iobj)')


def part2(rows, iobj):

  return

#util.output.pretty_answer('P1', part1(rows, iobj))
#util.output.pretty_answer('P2', part2(rows, iobj))
