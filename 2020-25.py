from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 25

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def tx(subject, loop):
  val = 1
  for i in range(loop):
    val *= subject
    val %= 20201227
  return val

def part1(rows, iobj):
  cpub = int(rows[0])
  dpub = int(rows[1])


  #cpub = tx(7, cloop)
  #dpub = tx(7, dloop) 

  val = 1
  for i in range(10_000_000):
    val *= 7
    val %= 20201227
    if val == cpub: 
      print(i)
      #return tx(dpub, i)

  #tx(dpub, cloop)
  #tx(cpub, dloop)

  print(tx(7, 5163354))

  return tx(dpub, 5163354)


  return

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
