from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 5

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

S = """
                [V]     [C]     [M]
[V]     [J]     [N]     [H]     [V]
[R] [F] [N]     [W]     [Z]     [N]
[H] [R] [D]     [Q] [M] [L]     [B]
[B] [C] [H] [V] [R] [C] [G]     [R]
[G] [G] [F] [S] [D] [H] [B] [R] [S]
[D] [N] [S] [D] [H] [G] [J] [J] [G]
[W] [J] [L] [J] [S] [P] [F] [S] [L]
 1   2   3   4   5   6   7   8   9 
"""

S = {
1: 'WDGBHRV',
2: 'JNGCRF',
3: 'LSFHDNJ',
4: 'JDSV',
5: 'SHDRQWNV',
6: 'PGHCM',
7: 'FJBGLZHC',
8: 'SJR',
9: 'LGSRBNVM',
}

for k in S:
  S[k] = list(S[k])

def part1(rows, iobj):

  for row in rows:
    if not row.startswith('move'): continue
    (n, src, dst) = ints(row)

    for i in range(n):
      v = S[src].pop()
      S[dst].append(v)


  for k in S:
    print(k, S[k])


  return ''.join(S[k][-1] for k in S)

def part2(rows, iobj):
  for row in rows:
    if not row.startswith('move'): continue
    (n, src, dst) = ints(row)

    move = []
    print(n, src, dst)
    for i in range(n):
      v = S[src].pop()
      move = [v] + move
    print(move)
    S[dst].extend(move)


  for k in S:
    print(k, S[k])
  return ''.join(S[k][-1] for k in S)

  return

# util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
