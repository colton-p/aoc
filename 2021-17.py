from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 17

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()






def part1(rows, iobj):

  tgt_x0, tgt_x1, tgt_y0, tgt_y1 = ints(ss)

  def sim(vx, vy):
    max_y = 0
    x = y = 0
    for i in range(6_010):
      x += vx
      y += vy
      max_y = max(y, max_y)
      if vx < 0:
        vx += 1
      elif vx > 0:
        vx -=1
      vy -= 1

      if tgt_x0 <= x <= tgt_x1 and tgt_y0 <= y <= tgt_y1:
        return True, max_y, i
      
      if y < tgt_y0 and vy < 0:
        return False, None, i
      if x > tgt_x1:
        return False, None, i
    
    print('!!!', vx, vy)
    return False, None, i


  best = 0
  cc = 0

  for (vx, vy) in itertools.product(range(0, 228), range(-135, 135)):
    rslt, goal, ix = sim(vx, vy)
    cc += ix
    if rslt:
      best = max(best, goal)
      if goal == best:
        pass
        # print(vx, vy, ix, best)



  return cc, best

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
