from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 17

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

HORZ = [(0,0), (1,0), (2, 0), (3, 0)]
CROSS = [(0,0), (1,0), (2, 0), (1, 1), (1, -1)]
ELL = [(0, 0), (1, 0), (2,0), (2,-1), (2,-2)]
BAR = [(0, 0), (0, -1), (0, -2), (0, -3)]
BOX = [(0, 0), (0, 1), (1, 1), (1, 0)]

def print_board(board):
  top_y = min(y for (x,y) in board)

  for y in range(top_y, 0):
    row = ''
    for x in range(0, 8):
      if x in [0, 9]:
        row += '|'
      elif (x,y) in board:
        row += '#'
      else:
        row += '.'
    print(row)
  print('+--------+')

def make_piece(board, shape, top_y):
  start_x = 3

  # assert top_y == min(y for (x,y) in board)
  offset_y = max(y for (x,y) in shape)
  start_y = top_y - 4 - offset_y

  start = (start_x, start_y)

  return tuple(
    vadd(start, offset) for offset in shape
  )

def shift_coords(piece, dir):
  return [
    vadd(dir, pt) for pt in piece
  ]

def check(board, piece):
  if any(pt in board for pt in piece):
    return False
  
  if any(x in [0, 8] for (x,y) in piece):
    return False
  
  return True

def drop_piece(board, piece, dir_it):
  while True:
    # try right
    shifted = shift_coords(piece, next(dir_it))
    if check(board, shifted):
      piece = shifted
    
    shifted = shift_coords(piece, DIR.DOWN)
    if check(board, shifted):
      piece = shifted
    else:
      break

  return piece
  
def part1(rows, iobj):
  board = { (x, 0) for x in range(8) }

  arrows = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
  arrows = iobj.single_string()
  print(len(arrows))
  dir_it = its.cycle({'>': DIR.RIGHT, '<': DIR.LEFT}[c] for c in arrows)
  shape_it = its.cycle([HORZ, CROSS, ELL, BAR, BOX])

  top_y = 0
  for i in range(90_000):
    shape = next(shape_it)
    piece = make_piece(board, shape, top_y)
    rslt = drop_piece(board, piece, dir_it)
    board |= set(rslt)

    top_y = min(top_y, min(y for (x,y) in rslt))

    yield (i+1, -top_y)
  
  #return min(y for (x,y) in board)

def part2(rows, iobj):

  it = part1(rows, iobj)

  H = defaultdict(int)
  for (blocks, height) in it:
    H[blocks] = height
  #          |--|--|
  # ---------------
  print(H[2022])
  print('x')
  offset = 50_000
  for step in range(5, 2_000):
    h0 = H[offset]
    heights = {
      H[offset + i*step] - H[offset + (i-1)*step] for i in [1,2, 3]
    }
    if len(heights) == 1:
      print(offset, step, heights)
      break
  
  print(step)

  tgt = 1000000000000 
  #tgt = 80_123
  v = (tgt - 50_000) % step
  print(v)
  dh = H[offset + step] - H[offset]
  print(dh)

  print('--')
  print(H[tgt])

  return H[offset] + (H[offset + v] -H[offset]) + dh * ((tgt-offset) // step)

  

  return

#util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
