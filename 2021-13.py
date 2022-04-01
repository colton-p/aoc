from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 13

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def fold_y(G, y):
  top = Grid({ k: v for(k,v) in G.grid.items() if k[1] < y})
  bot = Grid({ k: v for(k,v) in G.grid.items() if k[1] > y})

  bot.flip_vertical()
  bot.translate(0, 2*y)

  return Grid({k: v for (k, v) in itertools.chain(top.grid.items(), bot.grid.items()) if v != '.'})

def fold_x(G, x):
  left = Grid({ k: v for(k,v) in G.grid.items() if k[0] < x})
  right = Grid({ k: v for(k,v) in G.grid.items() if k[0] > x})

  right.flip_horizontal()
  #left.recenter()
  right.translate(2*x, 0)

  return Grid({k: v for (k, v) in itertools.chain(left.grid.items(), right.grid.items()) if v != '.'})

def part1(rows, iobj):

  (pts, instr) = iobj.line_delimited()

  G = Grid.from_rows([])
  for line in pts:
    (x,y) = ints(line)
    G.grid[(x,y)] = '#'
  
  print(len(G.grid))

  for ss in instr:
    func = ss.split('=')[0][-1]
    (val,) = ints(ss)
    print(func, val)

    if func == 'x':
      G = fold_x(G, val)
    else:
      G = fold_y(G, val)
    # G.recenter()
    print(G.min_x(), G.max_x())
    
  print(G.to_s())

  return 

  H = fold_x(G, 655)
  #H = fold_y(G, 7)
  #H = fold_x(H, 5)

  print(H.to_s())

  return H.count('#')

  #print(G.to_s())
  #print('')

  #H = fold_y(G, 7)
  #print(H.to_s())
  #print('')
  #H = fold_x(H, 5)
  #print(H.to_s())





  return

def part2(rows, iobj):
  (pts, folds) = iobj.line_delimited()

  G = {}
  for line in pts:
    pt = tuple(ints(line))
    G[pt] = '#'
  
  for fold in folds:
    print(fold)

  return

#util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
