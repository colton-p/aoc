from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 12

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def _build_goal_fn(goal):
  if callable(goal):
    return goal
  elif goal is not None:
    return lambda x: (x == goal)
  else:
    return None

def lower(x):
  return x.lower() == x

def xdfs(start, adjacent_fn, goal=None):
  """
  Depth-first search
  """
  goal_fn = _build_goal_fn(goal)
  stack = collections.deque()

  stack.append(start)
  visited = set()
  parent_map = {start: None}

  paths = set()

  while len(stack):
    print(stack)
    v = stack[-1]
    if lower(v) and v in visited: continue
    visited.add(v)

    for child_state in reversed(sorted(adjacent_fn(v))):
      if child_state not in parent_map:
          parent_map[child_state] = v

      if child_state not in stack:
        stack.append(child_state)

      if child_state == 'end':
        paths.add(tuple(stack))
        stack.pop()

  assert set(parent_map.keys()) == visited
  return paths, parent_map

def search(path, adjacent_fn, cc):

  node = path[-1]
  for child in sorted(adjacent_fn(node)):

    #if child == 'start' and cc['start'] >= 1: continue
    #if lower(child) and cc[child] >= 2: continue
    if child == 'start' and child in path: continue
    if lower(child) and cc[child] >= 2: continue

    pp = list(path) + [child]
    cc2 = Counter(cc)
    cc2[child] += 1
    if sum(lower(k) and v >= 2 for (k,v) in cc2.items()) > 1:
      continue


    if child == 'end':
      yield pp
    else:
      for x in search(pp, adjacent_fn, cc2):
        yield x
  return





def part1(rows, iobj):
  G = nx.Graph()
  ADJ = defaultdict(set)
  for row in rows:
    (s, t) = row.split('-')
    G.add_edge(s, t)
    ADJ[s].add(t)
    ADJ[t].add(s)
  

  rslt = search(['start'], lambda x: ADJ[x], Counter(['start']))

  # rslt = [tuple(x) for x in rslt]

  c = 0
  for (ix,x) in enumerate(sorted(rslt)):

    C = Counter(x)
    if sum(lower(k) and v >= 2 for (k,v) in C.items()) > 1:
      continue
    # print(ix, x) 
    c += 1

  return c
  print(nx.info(G))

  H = nx.Graph()

  to_contract = [node for node in G.nodes if node.upper() == node]
  print(to_contract)
  for x in to_contract:
    y = list(G.neighbors(x))[0]
    G = nx.contracted_nodes(G, y, x) 
    
  print(nx.info(G))

  print(G.nodes())

  for p in nx.all_simple_paths(G, 'start', 'end'):
    print(p)



  return

def tx(G):
  H = nx.Graph()
  to_expand = {v for v in G.nodes if not lower(v)}
  to_keep = set(G.nodes) - to_expand
  print(to_keep)
  print(to_expand)
  print('--')

  H.add_nodes_from(to_keep)
  for (s,t) in G.edges:
    if s in to_keep and t in to_keep:
      H.add_edge(s, t)
  
  new_edges = set()
  for v in to_expand:
    new_edges |= set(itertools.combinations(nx.neighbors(G, v), 2))
  H.add_edges_from(new_edges)
  
  return H, new_edges




def part2(rows, iobj):
  H = nx.Graph()
  H.add_edges_from([row.split('-') for row in rows])
  #H, ee = tx(H)
  ee = set()

  for e in ee:
    print(e)

  
  def tx_path(path0):
    to_add = set()
    for (ix, (s,t)) in enumerate(each_cons(path0)):
      if (s,t) in ee:
        to_add.add(ix)
    
    for ss in powerset(to_add):
      path = list(path0)
      for ix in reversed(sorted(ss)):
        path = path[:ix+1] + ['A'] + path[ix+1:]
      yield path


  print('')
  cc = 0
  for p in nx.all_simple_paths(H, 'start', 'end'):
    print(p)
    #for pp in tx_path(p):
    #  cc += 1
    #  print('\t', cc, pp)




  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
