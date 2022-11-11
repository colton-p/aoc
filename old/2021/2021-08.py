from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 8

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

MM = {
  0: 'ABCEFG',
  1: 'CF',
  2: 'ACDEG',
  3: 'ACDFG',
  4: 'BCDF',
  5: 'ABDFG',
  6: 'ABDEFG',
  7: 'ACF',
  8: 'ABCDEFG',
  9: 'ABCDFG',
}
MM = {v:k for (k,v) in MM.items()}

def figure(left, right):
  A = {}

  (one,) = [v for v in left if len(v) == 2]
  (seven,) = [v for v in left if len(v) == 3]
  (four,) = [v for v in left if len(v) == 4]
  (eight,) = [v for v in left if len(v) == 7]
  # print('4', four)
  # print('1', one)
  # print('7', seven)
  A['A'] = set(seven)-set(one)
  (three,) = [v for v in left if len(v) == 5 and set(one) < set(v)]
  # print('3', three)
  A['G'] = set(three) - set(seven) - set(four)
  A['B'] = set(four) - set(three)

  A['D'] = set(four) - A['B'] - set(one)


  A['E'] = set(eight) - set(three) - A['B']



  (two,) = [v for v in left if len(v) == 5 and (not(A['B'] & set(v))) and (A['E'] & set(v))]
  A['F'] = set(one) - set(two)
  A['C'] = set(one) - A['F']

  M = {list(v)[0]: k for (k,v) in A.items()}

  for code in right:
    yield str(MM[''.join(sorted(M[c] for c in code))])

  #print(A) 









def part1(rows, iobj):

  r = 0
  for row in rows:
    (left, right) = row.split(' | ')
    left = left.split(' ')
    right = right.split(' ')

    r += int(''.join(figure(left, right)))

    #c = Counter(len(v) for v in right)

    #r += c[2] + c[4] + c[3] + c[7] 



  return r

def part2(rows, iobj):

  def gen():
    for big in itertools.permutations('ABCDEFG'):
      yield {k: v for (k,v) in zip('abcdefg', big)}

  correct_segs = { frozenset(s) for s in MM }
  def chk(perm, left):
    for l in left:
      mapped = frozenset(perm[c] for c in l)
      if mapped not in correct_segs:
        return False
    return True
  
  def ev(perm, code):
    segs = ''.join(sorted(perm[c] for c in code))
    return str(MM[segs])

  def xlate(left, right):
    for perm in gen():
      if chk(perm, left):
        break
    
    n_str = ''.join(ev(perm, code) for code in right)
    return int(n_str)

  r = 0
  for row in rows:
    (left, right) = row.split(' | ')
    left = left.split(' ')
    right = right.split(' ')
    r += xlate(left, right)

  return r

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
