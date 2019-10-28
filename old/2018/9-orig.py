#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print('Day 9')
print('------')

rows = input_rows('9', test=False)

(n_players, n_marbles) = map(int, re.findall('\d+', rows[0]))

n_marbles *= 100

scores = defaultdict(int)
L = [0]
current_ix = 0

marble_iter = range(1, n_marbles + 1)
player_iter = itertools.cycle(range(1, n_players + 1))

for (marble, player) in zip(marble_iter, player_iter):
  if marble % 10000 == 0:
    print(marble)
  if marble % 23 != 0:
    insert_ix = (current_ix + 1) % len(L) + 1
    L.insert(insert_ix, marble)
    current_ix = insert_ix
  else:
    scores[player] += marble
    delete_ix = (current_ix - 7 + len(L)) % (len(L))
    scores[player] += L[delete_ix]
    del L[delete_ix]
    current_ix = delete_ix
  #print player, ''.join(['(%2d)' % i if i == L[current_ix] else '%4d' % i for i in L])

print(max(scores.values()))
