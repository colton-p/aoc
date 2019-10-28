from itertools import *
import collections
import hashlib
import re

import requests
import os.path

def input_rows(day, test=False, strip = True):
  path = '%s.in' % (day)

  if test: path += '.test'

  if not os.path.exists(path):
    print('Fetching new input...')
    input_url = 'https://adventofcode.com/2018/day/%s/input' % (day)
    input = requests.get(input_url, cookies={'session': open('.aoc_session').read().strip()}).text
    with open(path, 'w') as f:
      f.write(input)

  with open(path, 'r') as f:
    if strip:
      return [line.strip() for line in f]
    else:
      return [line for line in f]

def old_input_rows(fname):
  with open(fname, 'r') as f:
    return [line.strip() for line in f]

def extract_numbers(line):
  """
  >>> extract_numbers('1 -2 3')
  [1, -2, 3]

  >>> extract_numbers('abc-12 - 34')
  [-12, 34]

  >>> extract_numbers('abcdef')
  []
  """
  return [int(x) for x in re.findall('-?\d+', line)]

def extract_number(line):
  """
  >>> extract_number('hi 123 bye')
  123
  >>> extract_number('oh no')
  Traceback (most recent call last):
  ...
  ValueError: need more than 0 values to unpack
  """
  (n,) = [int(x) for x in re.findall('-?\d+', line)]
  return n


def split_rows(rows, regex=None, sep=None):
  """
  >>> split_rows(['1-2-3', '4-5-6'], sep='-')
  [('1', '2', '3'), ('4', '5', '6')]
  >>> split_rows(['1-2-3', '4-5-6'], regex='(\d-\d)-(\d)')
  [('1-2', '3'), ('4-5', '6')]
  """
  def g():
    for row in rows:
      if regex:
        m = re.match(regex, row)
        yield m.groups()
      elif sep:
        yield tuple(row.split(sep))
      else:
        yield (row,)
  return [x for x in g()]



#### ####
# sketch countings
#### ####

def count_with_predicate(lines, predicate):
  """
  >>> count_with_predicate(['abc', 'def', 'axy'], lambda x: x.startswith('a'))
  2
  """
  return sum_with_predicate(lines, lambda line: (predicate(line), 1))

def sum_matching(lines, regex):
  """
  >>> sum_matching(['a-1', 'b-2', 'c-3'], '[ac]-(\d)')
  4

  >>> sum_matching(['a-x', 'b-2', 'c-3'], '[ac]-(\d)')
  3
  """

  def f(line):
    m = capture(regex, line)
    return (bool(m), m and int(m[0]) or 0)
  return sum_with_predicate(lines, f)


def sum_with_predicate(lines, predicate):
  """
  >>> sum_with_predicate(['abc', 'def', 'axy'], lambda x: (x.startswith('a'), 1))
  2
  """

  s = 0
  for line in lines:
    (incl, val) = predicate(line)
    if incl:
      s += val
  return s


#### ####
#
# Grids
#
#### ####
def rows_to_grid(rows):
  """
     0123
     j--->
  i 0....
  | 1....
  | 2....
  v 3....

  >>> rows_to_grid([ [1, 2, 3], [4, 5, 6] ])
  {(0, 1): 2, (1, 2): 6, (0, 0): 1, (1, 1): 5, (1, 0): 4, (0, 2): 3}

    1 4
    2 5
    3 6
  """

  grid = {}
  for (i, row) in enumerate(rows):
    for (j, v) in enumerate(row):
      grid[(i,j)] = v
  return grid

def print_grid(grid):
  max_x = max(grid.keys(), key=lambda x:x[0])[0]
  max_y = max(grid.keys(), key=lambda x:x[1])[1]

  min_x = min(grid.keys(), key=lambda x:x[0])[0]
  min_y = min(grid.keys(), key=lambda x:x[1])[1]
  print min_x, max_x
  print min_y, max_y
  print (max_x-min_x), (max_y-min_y)
  print (max_x-min_x)*(max_y-min_y)

  for j in range(min_y, max_y+1):
    for i in range(min_x, max_x+1):
      print '%1s' % (grid[(i,j)]),
    print('')

def rect_adj(pt, diag=False):
  """
  >>> list(rect_adj((0,0)))
  [(0, 1), (0, -1), (1, 0), (-1, 0)]
  """
  (x,y) = pt
  for (i,j) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    yield (x+i, y+j)
  if diag:
    for (i,j) in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
      yield (x+i, y+j)

def rect_adj_bounds(pt, min_x, max_x, min_y, max_y, diag=False):
  """
  >>> list(rect_adj_bounds((0,0), 0, 100, 0, 100))
  [(0, 1), (1, 0)]
  """
  for (x, y) in rect_adj(pt, diag):
    if min_x <= x <= max_x and min_y <= y <= max_y:
      yield (x,y)

#### ####
#
# Itertools tricks
#
#### ####
def transpose(rows):
  """
  >>> transpose([ [1, 2, 3], [4, 5, 6] ])
  [[1, 4], [2, 5], [3, 6]]
  """
  return [ [row[i] for row in rows] for i in range(len(rows[0]))]

def powerset(iterable):
  """
  >>> list(powerset([1,2,3]))
  [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
  """
  s = list(iterable)
  return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def pairwise(iterable):
  """s -> (s0,s1), (s1,s2), (s2, s3), ...

  >>> list(pairwise([1, 2, 3, 4]))
  [(1, 2), (2, 3), (3, 4)]
  """
  a, b = tee(iterable)
  next(b, None)
  return izip(a, b)

def grouper(iterable, n, fillvalue=None):
  """Collect data into fixed-length chunks or blocks
  >>> list(grouper('ABCDEFG', 3, 'x'))
  [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]
  """
  args = [iter(iterable)] * n
  return izip_longest(fillvalue=fillvalue, *args)

#### ####
#
# Rotates and shifts
#
#### ####

def hash_digest(x, algo='md5'):
  """Hash hexdigest

  >>> hash_digest("The quick brown fox jumps over the lazy dog")
  '9e107d9d372bb6826bd81d3542a419d6'
  """
  h = hashlib.new(algo)
  h.update(x)
  return h.hexdigest()

def hash_func(algo='md5'):
  """Hash as one-arg function
  >>> hash_func()("The quick brown fox jumps over the lazy dog")
  '9e107d9d372bb6826bd81d3542a419d6'
  """
  return lambda x: hash_digest(x, algo)

def rotate_string(s, n=13):
  """ROT-13 encoding

  >>> rotate_string('abc-KLM')
  'nop-XYZ'
  >>> rotate_string('abc', 3)
  'def'
  """

  a = 'abcdefghijklmnopqrstuvwxyz'
  A = a.upper()

  def f(c):
    if c not in a+A:
      return c
    if c in a:
      return a[(a.index(c) + n) % len(a)]
    if c in A:
      return A[(A.index(c) + n) % len(A)]

  return ''.join([f(c) for c in s])

def head(L, n):
  """
  >>> head([1,2,3,4,5], 2)
  [1, 2]
  >>> head([1,2, 3], 100)
  [1, 2, 3]
  """
  return L[:n]

def tail(L, n):
  """
  >>> tail([1,2,3,4,5], 2)
  [4, 5]
  >>> tail([1], 2)
  [1]
  """
  return L[-n:]

def rotate_right(L, k):
  """
  >>> rotate_right([1, 2, 3, 4], 1)
  [4, 1, 2, 3]
  """
  return L[-k:] + L[:-k]

def rotate_left(L, k):
  """
  >>> rotate_left([1, 2, 3, 4], 1)
  [2, 3, 4, 1]
  """
  return L[k:] + L[:k]

def insert_after(L, ix, val):
  """
  >>> insert_after([1, 2, 3, 4], 2, 'X')
  [1, 2, 3, 'X', 4]
  """
  return L[:ix+1] + [val] + L[ix+1:]

def insert_before(L, ix, val):
  """
  >>> insert_before([1, 2, 3, 4], 2, 'X')
  [1, 2, 'X', 3, 4]
  """
  return L[:ix] + [val] + L[ix:]

def join(it, sep=''):
  """
  >>> join(['1', '2', '3'], '-')
  '1-2-3'
  """
  return sep.join(it)


#### ####
#
# Algorithms
#
#### ####

def dfs(start=None, adjacent_fn=None, goal_fn=None):
  """
  >>> G = {\
    1: [2, 3, 6],\
    2: [1, 3, 4],\
    3: [1, 6, 2],\
    4: [2, 3, 5],\
    5: [4, 6],\
    6: [1, 3, 5],\
  }; dfs(1, lambda x: G[x], lambda x: x == 6)
  {1: None, 2: 1, 3: 1, 6: 1}
  """
  S = collections.deque()

  S.append(start)
  visited = set()
  pr = {start: None}

  while not len(S) == 0:
    v = S.pop()
    if v not in visited:
      visited.add(v)
      for child_state in adjacent_fn(v):
        if child_state not in pr:
          pr[child_state] = v
        if goal_fn(child_state):
          return pr
        S.append(child_state)
  assert set(pr.keys()) == visited
  return pr

def connected_components(nodes, adjacent_fn=None):
  """
  >>> connected_components(range(1, 11), lambda x: [y for y in range(1, 11) if y % 3 == x % 3])
  [(1, 10, 4, 7), (8, 2, 5), (9, 3, 6)]
  """
  components = []
  to_visit = set(nodes)

  while to_visit:
    start = to_visit.pop()
    pr = dfs(start, adjacent_fn, lambda x: False)
    to_visit -= set(pr.keys())
    components += [pr.keys()]
  return map(tuple, components)



def dijkstra(vertices, start=None, adjacent_fn=None):
  """
  >>> G = {\
    1: [(2, 7), (3,9), (6,14)],\
    2: [(1, 7), (3,10), (4,15)],\
    3: [(1, 9), (6,2), (2,10)],\
    4: [(2, 15), (3,11), (5,6)],\
    5: [(4,6), (6,9)],\
    6: [(1,14), (3,2), (5,9)],\
  }; dijkstra(G.keys(), 1, lambda x: G[x])
  ({1: 0, 2: 7, 3: 9, 4: 22, 5: 20, 6: 11}, {1: None, 2: 1, 3: 1, 4: 2, 5: 6, 6: 3})
  """

  seen = set()
  Q = set()
  dist = {}
  prev = {}
  for v in vertices:
    dist[v] = 99999999999999
    prev[v] = None
    Q.add(v)

  dist[start] = 0

  while len(Q) != 0:
    u = min(Q, key=lambda v: dist[v])

    Q.remove(u)
    seen.add(u)

    for (v, weight) in adjacent_fn(u):
      if v in seen:
        continue
      alt = dist[u] + weight
      if alt < dist[v]:
        dist[v] = alt
        prev[v] = u

  return dist, prev

from heapdict import heapdict


def dijkstra2(vertices, start=None, adjacent_fn=None, target=None):
  """
  >>> G = {\
    1: [(2, 7), (3,9), (6,14)],\
    2: [(1, 7), (3,10), (4,15)],\
    3: [(1, 9), (6,2), (2,10)],\
    4: [(2, 15), (3,11), (5,6)],\
    5: [(4,6), (6,9)],\
    6: [(1,14), (3,2), (5,9)],\
  }; dijkstra2(G.keys(), 1, lambda x: G[x])
  ({1: 0, 2: 7, 3: 9, 4: 22, 5: 20, 6: 11}, {})
  """

  Q = heapdict()
  dist = {}
  prev = {}
  seen = set()
  for v in vertices:
    dist[v] = 99999999999999
    #Q[v] = dist[v]

  Q[start] = 0
  dist[start]=0

  while len(Q) != 0:
    (u, _) = Q.popitem()

    if target is not None and target == u:
      return dist, {}

    seen.add(u)

    for (v, weight) in adjacent_fn(u):
      if v in seen:
        continue
      Q[v] = dist[v]

      alt = dist[u] + weight
      if alt < dist[v]:
        dist[v] = alt
        Q[v] = dist[v]

  return dist, prev

def dijkstra3(vertices, start=None, adjacent_fn=None):
  """
  >>> G = {\
    1: [(2, 7), (3,9), (6,14)],\
    2: [(1, 7), (3,10), (4,15)],\
    3: [(1, 9), (6,2), (2,10)],\
    4: [(2, 15), (3,11), (5,6)],\
    5: [(4,6), (6,9)],\
    6: [(1,14), (3,2), (5,9)],\
  }; dijkstra3(G.keys(), 1, lambda x: G[x])
  ({1: 0, 2: 7, 3: 9, 4: 22, 5: 20, 6: 11}, {})
  """

  seen = set()
  Q = set()
  dist = {}
  prev = {}
  for v in vertices:
    dist[v] = 99999999999999
    #Q.add(v)

  dist[start] = 0
  Q.add(start)

  while len(Q) != 0:
    u = min(Q, key=lambda v: dist[v])

    Q.remove(u)
    seen.add(u)

    for (v, weight) in adjacent_fn(u):
      if v in seen:
        continue
      Q.add(v)
      alt = dist[u] + weight
      if alt < dist[v]:
        dist[v] = alt

  return dist, {}



def integer_partitions(n, k, l=1):
  """Integer partitions of n of size k, each element being at least l
  >>> list(integer_partitions(5, 3))
  [(1, 1, 3), (1, 2, 2), (1, 3, 1), (2, 1, 2), (2, 2, 1), (3, 1, 1)]

  >>> list(integer_partitions(6, 2, l=2))
  [(2, 4), (3, 3), (4, 2)]
  """
  if k < 1:
    return
  if k == 1:
    if n >= l:
      yield (n,)
    return

  for i in range(l, n):
    for r in integer_partitions(n-i, k-1, l):
      yield (i,) + r

def knapsack(values, weights, W):
  """
  Maximum sum(value) with sum(weight) <= W
  Returns (list of value indexes, total value)

  >>> knapsack([4, 2, 2, 1, 10], [12, 2, 1, 1, 4], 15)
  ([2, 2, 2, 4, 4, 4], 36)
  """
  m = {}

  N = len(values)

  m[0] = 0
  c = collections.defaultdict(list)

  for w in range(W+1):
    seq = [i for i in range(N) if weights[i] <= w]
    if seq:
      ix = max(seq, key=lambda j: values[j] + m[w-weights[j]])
      m[w] = values[ix] + m[w-weights[ix]]
      c[w] = [ix] + c[w-weights[ix]]

  return c[W], m[W]


########

def bfs(start=None, adjacent_fn=None, goal_fn=None, passable_fn=lambda x: True):

  open_set = collections.deque()
  closed_set = set()

  # a dictionary to maintain meta information (used for path formation)
  meta = dict()  # key -> (parent state, action to reach child)

  # initialize
  meta[start] = (None)
  open_set.append(start)

  while len(open_set) > 0:

    parent_state = open_set.popleft()

    if goal_fn(parent_state):
      return construct_path(parent_state, meta)

    for child_state in adjacent_fn(parent_state):

      if child_state in closed_set:
        continue

      if child_state not in open_set:
        meta[child_state] = parent_state
        open_set.append(child_state)

    closed_set.add(parent_state)

def construct_path(state, meta):
  path = []

  while state in meta:
    path.append(state)
    state = meta[state]

  return list(reversed(path))

#######
# TODO: kill this
def match(regex, line):
  """
  >>> match('ab+', 'a')
  False
  >>> match('ab+', 'abbbb')
  True
  >>> match('ab', 'XXXab')
  False
  """

  m = re.match(regex, line)
  return m is not None

def capture(regex, line):
  """
  >>> capture('a-(\d+)-(\d+)', 'a-123-456')
  ('123', '456')
  >>> capture('a-(\d+)-(\d+)', 'X-123-456')
  False
  >>> capture('(\w+)\s+(\w+)', 'abc1    X_YZ')
  ('abc1', 'X_YZ')
  """
  m = re.match(regex, line)
  if m is None:
    return False
  return m.groups()





if __name__ == '__main__':
  import doctest
  doctest.testmod()



