import itertools as its
import re
import math
import operator as op

#from util import *
import util.output
from util import Input

YEAR = 2021
DAY = 23
iobj = Input.for_date(DAY, year=YEAR, test=False)


TGT_X = { 'A': (2, 23, 19, 15, 11), 'B': (4, 24, 20, 16, 12), 'C': (6, 25, 21, 17, 13), 'D': (8, 26, 22, 18, 14) }
ENERGY = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

D = {
  (0, 11): 3,
  (0, 12): 5,
  (0, 13): 7,
  (0, 14): 9,
  (0, 15): 4,
  (0, 16): 6,
  (0, 17): 8,
  (0, 18): 10,

  (1, 11): 2,
  (1, 12): 4,
  (1, 13): 6,
  (1, 14): 8,
  (1, 15): 3,
  (1, 16): 5,
  (1, 17): 7,
  (1, 18): 9,

  (3, 11): 2,
  (3, 12): 2,
  (3, 13): 4,
  (3, 14): 6,
  (3, 15): 3,
  (3, 16): 3,
  (3, 17): 5,
  (3, 18): 7,

  (5, 11): 4,
  (5, 12): 2,
  (5, 13): 2,
  (5, 14): 4,
  (5, 15): 5,
  (5, 16): 3,
  (5, 17): 3,
  (5, 18): 5,

  (7, 11): 6,
  (7, 12): 4,
  (7, 13): 2,
  (7, 14): 2,
  (7, 15): 7,
  (7, 16): 5,
  (7, 17): 3,
  (7, 18): 3,

  (9, 11): 8,
  (9, 12): 6,
  (9, 13): 4,
  (9, 14): 2,
  (9, 15): 9,
  (9, 16): 7,
  (9, 17): 5,
  (9, 18): 3,

  (10, 11): 9,
  (10, 12): 7,
  (10, 13): 5,
  (10, 14): 3,
  (10, 15): 10,
  (10, 16): 8,
  (10, 17): 6,
  (10, 18): 4,

  (11, 12): 4,
  (11, 16): 5,
  (11, 13): 6,
  (11, 17): 7,
  (11, 14): 8,
  (11, 18): 9,

  (12, 13): 4,
  (12, 14): 6,
  (12, 15): 5,
  (12, 17): 5,
  (12, 18): 7,

  (13, 14): 4,
  (13, 15): 6,
  (13, 16): 5,
  (13, 18): 5,

  (14, 15): 9,
  (14, 16): 7,
  (14, 17): 5,

  (15, 16): 6,
  (15, 17): 8,
  (15, 18): 10,

  (16, 17): 6,
  (16, 18): 8,

  (17, 18): 6,
}

class State:
#  0 1 2 3  4 5 6 7 8 9 10
#     11   12  13  14
#     15   16  17  18
#     19   20  21  22
#     23   24  25  26

  @classmethod
  def from_rows(cls, rows):
    board = list(rows[1][1:-1])
    board += [c for c in rows[2] if c in 'ABCDabcd.']
    board += [c for c in rows[3] if c in 'ABCDabcd.']
    board += [c for c in rows[4] if c in 'ABCDabcd.']
    board += [c for c in rows[5] if c in 'ABCDabcd.']


    home = frozenset(ix for (ix, c) in enumerate(board) if c in 'abcd')
    board = tuple(c.upper() for c in board)

    assert len(board) == 27, len(board)
    return cls(tuple(board), home)




  def __init__(self, board, home):
      self.board = board
      self.home = home
  
  def __hash__(self):
    return hash((self.board, self.home))
  
  def __eq__(self, other):
    return self.board == other.board and self.home == other.home
    
  def __str__(self):
    s = ' '
    s += ''.join(self.board[:11])
    s += '\n   ' + ' '.join(self.board[ix].lower() if ix in self.home else self.board[ix] for ix in range(11, 15))
    s += '\n   ' + ' '.join(self.board[ix].lower() if ix in self.home else self.board[ix] for ix in range(15, 19))
    s += '\n   ' + ' '.join(self.board[ix].lower() if ix in self.home else self.board[ix] for ix in range(19, 23))
    s += '\n   ' + ' '.join(self.board[ix].lower() if ix in self.home else self.board[ix] for ix in range(23, 27))

    assert all(c in 'ABCD.' for c in self.board)

    return s
  
  def swap(self, src, dst, home=False):
    new_board = list(self.board)
    new_board[src], new_board[dst] = self.board[dst], self.board[src]
    if home:
      new_home = self.home | frozenset([dst])
    else:
      new_home = self.home
    return State(tuple(new_board), new_home)

  def move_to_room(self, src):
    assert 0 <= src <= 10
    assert self.board[src] != '.'
    val = self.board[src]

    (tgt_x, *home_cells) = TGT_X[val]

    if any(self.board[ix] != '.' for ix in range(1+min(tgt_x, src), max(tgt_x, src))):
      return None, 'not clear'
    
    for (home_ix, dst) in enumerate(home_cells):
      if self.board[dst] == val:
        continue
      if self.board[dst] != '.':
        assert self.board[dst] in set('ABCD') - set(val)
        return None, None
      assert self.board[dst] == '.'

      steps = (4 - home_ix) + abs(tgt_x - src)
      return self.swap(src, dst, home=True), (steps) * ENERGY[val]
    assert False

  def move_to_hall(self, src):
    assert 11 <= src <= 26
    assert self.board[src] != '.'
    val = self.board[src]
    ee = ENERGY[val]
    return [
      (self.swap(src, dst), w * ee) for (dst, w) in self.move_to_hall_targets(src)
    ]


  def move_to_hall_targets(self, src):
    assert 11 <= src <= 26
    assert self.board[src] != '.'
    assert self.board[src] in 'ABCD'
    assert src not in self.home
    val = self.board[src]

    (tgt_x, *home_cells) = TGT_X[val]

    steps = 1
    ix = src - 4
    while ix >= 11:
      steps += 1
      if self.board[ix] != '.':
        return None, None
      ix -= 4
    tgt_x = 2*(ix - 6)
    assert tgt_x in {2, 4, 6, 8}

    for ix in range(tgt_x-1, -1, -1):
      if ix in [2,4,6,8]: continue
      if self.board[ix] != '.':
        break
      yield ix,  steps + tgt_x - ix #D[(ix, src)]

    for ix in range(tgt_x+1, 11, 1):
      if ix in [2,4,6,8]: continue
      if self.board[ix] != '.':
        break
      yield ix,  steps + ix - tgt_x #D[(ix, src)]


  def adj(self):
    for src in range(0, 11):
      if self.board[src] == '.':
        continue
      (rslt, w) = self.move_to_room(src)
      if rslt:
        yield (rslt, w)
    
    for src in range(11, 8+19):
      if self.board[src] == '.':
        continue
      if src in self.home:
        continue
      for (rslt, w) in self.move_to_hall(src):
        yield (rslt, w)

  def h(self):
    return 0
    s = 0
    for src in range(0, 11):
      val = self.board[src]
      if val == '.': continue
      tgt = TGT_X[val][1]
      s += D[(src, tgt)] * ENERGY[val]
    
    for src in range(11, 19):
      val = self.board[src]
      if val == '.': continue
      (tgt_x, *home_cells) = TGT_X[val]
      if src in home_cells: continue
      tgt = home_cells[0]

      s += D[min(src, tgt), max(src, tgt)] * ENERGY[val]

    return s



GOAL = State(tuple('...........ABCDABCDABCDABCD'), home=frozenset(range(11, 8+19)))
S0 = State.from_rows(iobj.rows)
S1 = State.from_rows(iobj.rows)

if 0:
  print(S0)
  for s, w in S0.adj():
    print(w)
    print(s)
    print('')

  exit()

import util.search
opt, path = util.search.shortest_path(S0, lambda x: x.adj(), GOAL, h_fn=lambda x: 0)
print(opt)
for x in path:
  print('')
  print(x[1])
  print(x[0])