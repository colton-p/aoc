from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 19

iobj = Input.for_date(DAY, year=YEAR, test=0)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()


RULES = {}

def match(rule, s):
  orig_s = str(s)
  if s == '':
    return None
  if len(rule) == 1:
    if rule[0] == 'a' or rule[0] == 'b':
      if s[0] == rule[0]:
        return 1
      else:
        return None
    else:
      for r in rule[0]:
        shift = match(RULES[r], s)
        if not shift: return None
        s = s[shift:]
      return len(orig_s) - len(s)
  else:
    (a, b) = rule

    return match([a], s) or match([b], s)

def mm(rule, s):
  return match(rule, s) == len(s)
  


def part1(rows, iobj):
  L = []
  for row in rows:
    if ':' in row:
      (ix, txt) = row.split(':')
      txt = txt.strip()
      ix = int(ix)
      if 'a' in txt or 'b' in txt:
        RULES[ix] = txt[1]
      elif '|' in txt:
        (l, r) = txt.split('|')
        RULES[ix] = (ints(l), ints(r))
      else:
        RULES[ix] = (ints(txt),)
    elif row == '':
      continue
    else:
      L += [row]
  
  A = set()
  B = set()

  for ll in range(1, 16):
    for t in itertools.product('ab', repeat=ll):
      s = ''.join(t)
      if mm(RULES[42], s):
        A.add(s)
      if mm(RULES[31], s):
        B.add(s)
  
  print('A', len(A), A)
  print('B', len(B), B)
  print(A & B)
  
  def mmm(s):
    t = ''
    for blk in each_slice(s, n=8):
      blk = ''.join(blk)
      if blk in A:
        t += 'A'
      if blk in B:
        t += 'B'
      if blk in A and blk in B:
        assert False, blk
      if blk not in A and blk not in B:
        assert False, blk
    
    print(s, t, t.count('A') > t.count('B') and bool(re.match('^A+A+B+$', t)))
    
    return t.count('A') > t.count('B') and bool(re.match('^A+A+B+$', t))
    
  c = 0
  for s in L:
    if mmm(s):
      c += 1
  
  

  return c
  #return quantify(L, lambda x: mm(RULES[0], x))

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
