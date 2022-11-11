from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 14

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()



def part1(rows, iobj):
  (tem, rules) = iobj.line_delimited()

  tem = list(tem[0])
  rules = [rule.split(' -> ') for rule in rules]

  rules = { (k[0], k[1]): v for (k,v) in rules}
  def ev(x):
    for (a,b) in each_cons(x):
      yield a
      assert (a,b) in rules
      if (a,b) in rules:
        yield rules[(a,b)]
    yield b

  for i in range(10):
    tem = list(ev(tem))
  C = Counter(tem)

  rslt = C.most_common()
  (_, hi) = rslt[0]
  (_, lo) = rslt[-1]

  return hi - lo




def part2(rows, iobj):
  (tem, rules) = iobj.line_delimited()

  tem = list(tem[0])
  rules = [rule.split(' -> ') for rule in rules]
  rules = { (k[0], k[1]): v for (k,v) in rules}

  C1 = Counter(tem)
  C2 = Counter(each_cons(tem))

  def ev(C1, C2):
    for ((a,c),val) in list(C2.items()):
      b = rules[(a,c)]
      C1[b] += val
      C2[(a,b)] += val
      C2[(b,c)] += val
      C2[(a,c)] -= val
    
    return C1, C2

  for i in range(40):
    C1, C2 = ev(C1, C2)

  rslt = C1.most_common()
  (_, hi) = rslt[0]
  (_, lo) = rslt[-1]


  return hi - lo

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
