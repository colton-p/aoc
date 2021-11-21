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

def p(x, n):
  return (x-1 + n) % n + 1

NN = 9
#NN = 1_000_000
def move(L, I):
  #print(L)
  dst = L[0]
  L.rotate(-1)
  M = []
  M += [L.popleft()]
  M += [L.popleft()]
  M += [L.popleft()]

  #print('pick', M)

  dsts = [p(dst - 1,NN), p(dst - 2,NN), p(dst - 3,NN), p(dst - 4,NN)]
  dst = [x for x in dsts if x not in M][0]
  #o_dst_ix = L.index(dst) + 1
  o_dst_ix = I[dst] - 3
  #print(dst, '->', o_dst_ix)
  #print(dst, '->', I[dst]-3)

  dst_ix = o_dst_ix
  #print('dst: %d @ %d' % (dst, dst_ix))

  dst_ix = dst_ix - (NN - 3)
  r_dst_ix = o_dst_ix - NN
  #print('->dst: %d @ %d' % (dst, dst_ix))

  # insert after dst
  L.rotate(-dst_ix)
  L.extendleft(reversed(M))
  L.rotate(r_dst_ix)

  #print(o_dst_ix)
  for k,v in I.items():
    if v == 0:
      I[k] = NN-1
    elif v == 1 or v == 2 or v == 3:
      I[k] += (o_dst_ix-1)
    elif v < o_dst_ix+4: 
      I[k] -= 4
    else:
      I[k] -= 1
  #print(sorted(I.items(), key=lambda x:x[1]))
  #I2 = {}
  #for (ix, x) in enumerate(L):
  #  I2[x] = ix
  #print(sorted(I2.items(), key=lambda x:x[1]))
      

  return L, I
  

import cProfile

def f(L, I):
  for i in range(100):
    L, I = move(L, I)
  return L


L = list(map(int, '389125467')) +  list(range(10, 1_000_000+1))
L = deque(L)
I = {}
for (ix, x) in enumerate(L):
  I[x] = ix
def part1(rows, iobj):

  # L = list(map(int, list(rows[0]))) + list(range(10, 1_000_000+1))
  L = list(map(int, '389125467'))# +  list(range(10, 1_000_000+1))
  
  #L =  list(range(1, 1_000_000+1))

  #L = [999_992, 999_993, 999_994] + [1, 6, 5, 2, 4] + list(range(11, 999_992, 4)) + list(range(999_995, 1000001)) + [8, 3, 7,9,10]
  #for i in range(12, 999_992, 4):
  #  L += [i+0, i+1, i+2]
  

  #print(L[:20])
  #print(L[-20:])
  #print(len(L))

  L = deque(L)


  #cur = 999_995


  cProfile.run('f(L, I)')

  return 
  for i in range(10):
    print('--', i+1, '--')
    print(L)
    L, I = move(L, I)
    print(L)


  return

  #for j in range(10):
  #  print(j * 100)
  #  for i in range(100):
      #print('')
      #print('--', i+1, '--')
      #L, I = move(L, I)
      #ix = L.index(1)
      #print(i, ix, list(L)[:30], list(L)[-10:])


  #ix = L.index(1)
  #L.rotate(-ix)
  #ix = L.index(1)
  #print(i, ix, list(L)[ix: ix+3], list(L)[-10:])

  # return L
  #return ''.join(map(str,L))[1:]

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
