from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 4

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def chk(board):
  for row_ix in range(len(board)):
    row = board[row_ix]
    if all(c == 'x' for c in row):
      return 'row', row_ix

  for col_ix in range(len(board[0])):
    if all(row[col_ix] == 'x' for row in board):
      return 'col', col_ix


def mark(board, n):
  for row_ix in range(len(board)):
    for col_ix in range(len(board[0])):
      if board[row_ix][col_ix] == n:
        board[row_ix][col_ix] = 'x'

def val(board):
  s = 0
  for row_ix in range(len(board)):
    for col_ix in range(len(board[0])):
      if board[row_ix][col_ix] != 'x':
        s += int(board[row_ix][col_ix])
  return s

def part1(rows, iobj):
  blks = iobj.line_delimited()

  calls = blks[0][0].split(',')
  boards = [ [re.split(' +', r) for r in b] for b in blks[1:]]

  for call in calls:
    for board in boards:
      mark(board, call)
    
    if len(boards) > 1:
      boards = [board for board in boards if not chk(board)]
    else:
      if chk(board):
        return val(boards[0]) * int(call)
  

def chk2(g):
  for row in range(g.nrows()):


def part2(rows, iobj):

  blks = iobj.line_delimited()

  rr = [re.split(' +', r) for r in blks[1]]
  print(rr)
  g = Grid.from_rows(rr)
  print(g.to_s(cell_size=3))

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
