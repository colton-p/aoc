import random
import itertools




ATest = {
  'HM': 1,
  'HG': 2,
  'LM': 1,
  'LG': 3,
  'E':  1
}

A0 = {
'PrG': 3, 'PrM': 3, 'RuG': 3, 'RuM': 3,
'PuM': 2, 'SrM': 2,
'ThG': 1, 'ThM': 1, 'PuG': 1, 'SrG': 1,
#'ElG': 1, 'ElM': 1, 'DiG': 1, 'DiM': 1,
'E': 1
}


def isSrcSafe(A, floor, parts):
  src_gens  = [k for (k,v) in A.iteritems() if v == floor and k.endswith('G') and k not in parts]
  src_chips = [k for (k,v) in A.iteritems() if v == floor and k.endswith('M') and k not in parts]

  if not src_gens:
    return True

  return all( ((chip[:-1]+'G') in src_gens) for chip in src_chips)


def isDstSafe(A, floor, parts):
  dst_parts = [k for (k,v) in A.iteritems() if v == floor and k != 'E'] + list(parts)
  dst_gens = [k for k in dst_parts if k.endswith('G')]
  dst_chips = [k for k in dst_parts if k.endswith('M')]

  if not dst_gens:
    return True

  return all( ((chip[:-1]+'G') in dst_gens) for chip in dst_chips)


def isSafe(A, src, dst, parts):
  assert abs(dst - src) == 1, (src, dst)

  return isSrcSafe(A, src, parts) and isDstSafe(A, dst, parts)

def move(A, dst, t_move):
  assert 'E' not in t_move
  assert len(t_move)
  assert abs(dst - A['E']) == 1
  for x in t_move:
    assert A[x] == A['E']

  assert isSafe(A, A['E'], dst, t_move)

  B = dict(A)
  for x in t_move:
    B[x] = dst
  B['E'] = dst
  return B

def adj(state):
  src = state['E']
  src_parts = [k for (k,v) in state.iteritems() if v == src and k != 'E']
  choices = list(itertools.combinations(src_parts, 1))
  choices += list(itertools.combinations(src_parts, 2))
  for dst in list(set([1,2,3,4]) & set([src + 1, src - 1])):
    for parts in choices:
      if isSafe(state, src, dst, parts):
        yield move(state, dst, parts)



def pp(A):
  for i in range(4, 0, -1):
    print i,
    print 'E' if A['E'] == i else '.',
    print '|',
    for k in sorted(A.keys()):
      if k != 'E':
        print '%3s' % (k if A[k] == i else '.'),
    print ''
  print ''

"""
A = dict(A0)

A = move(A, 2, ['PuG', 'SrG'])
A = move(A, 3, ['PuG', 'PuM'])
A = move(A, 4, ['PuG', 'PuM'])
A = move(A, 3, ['PuG'])
A = move(A, 2, ['PuG'])
A = move(A, 3, ['PuG', 'SrG'])
A = move(A, 4, ['PuG', 'SrG'])
A = move(A, 3, ['SrG'])
A = move(A, 2, ['RuM', 'PrM'])
A = move(A, 3, ['SrM'])
A = move(A, 4, ['RuG', 'PrG'])
A = move(A, 3, ['RuG'])
A = move(A, 4, ['SrG', 'SrM'])
A = move(A, 3, ['PrG'])
A = move(A, 2, ['RuG', 'PrG'])
A = move(A, 3, ['RuM', 'PrM'])
A = move(A, 2, ['RuM'])
A = move(A, 3, ['RuG', 'PrG'])
A = move(A, 4, ['RuG', 'PrG'])
A = move(A, 3, ['PrG'])
A = move(A, 2, ['PrM'])
pp(A)
"""



best = None
visited = dict()
score = lambda kk: 56 - sum(flr if obj != 'E' else 0 for (obj,flr) in kk)
def search(state, depth):
  global best
  k_state = frozenset(state.items())

  if k_state in visited and visited[k_state] < depth:
    depth = visited[k_state]
    return
  else:
    visited[k_state] = depth

  if depth + visited[k_state] > 97:
    return

  if (score(state.items()), depth) < (best[1], best[2]):
    best = (state, score(state.items()), depth)
    print '*', (best[0], best[1], best[2])

  l = list(adj(state))
  if not l:
    return
  new_state = random.choice(list(adj(state)))
  search(new_state, depth+1)


qqq = 0
to_visit = []
best = (0, 10000, 10000)
def search2(state, depth):
  global qqq, best, to_visit

  #print state, depth
  if depth > qqq:
    qqq = depth
    print score(state.items()), depth, len(to_visit)
  k_state = frozenset(state.items())
  if k_state in visited and visited[k_state] < depth:
    return
  else:
    visited[k_state] = depth

  if ( (score(state.items()), depth) < (best[1], best[2])):
    best = (state, score(state.items()), depth)
    print '*', best

  to_visit += [(s, 1+depth) for s in (adj(state))]

#to_visit =[(A0, 0)]
#while to_visit:
#  search2(*to_visit.pop(0))

import heapq

def AA(start):
  closedSet = set([])
  openSet = set([(frozenset(start.items()))])

  estimate = lambda kk: 56-sum(flr if obj != 'E' else 0 for (obj,flr) in kk)
  gScore = {}
  fScore = {}
  gScore[frozenset(start.items())] = 0
  fScore[frozenset(start.items())] = estimate(start.items())

  while openSet:
    k_current = min(openSet, key=lambda x: fScore.get(x, None))
    current = dict(k_current)

    openSet.remove(k_current)
    closedSet.add(k_current)

    if len(openSet) > 1000:
      openSet = set(sorted(openSet, key=lambda x: fScore.get(x, None))[:100])

    if len(closedSet) % 1000 == 0:
      print len(openSet), len(closedSet), estimate(k_current), fScore[k_current], gScore[k_current]
    if estimate(k_current) == 0:
      return

    for neighbor in adj(current):
      k_neighbor = frozenset(neighbor.items())
      if k_neighbor in closedSet:
        continue
      gscore = gScore[k_current] + 1
      if k_neighbor not in openSet:
        openSet.add(k_neighbor)
      elif gscore > gScore.get(k_neighbor,None):
        continue

      gScore[k_neighbor] = gscore
      fScore[k_neighbor] = gscore + estimate(k_neighbor)

  assert False

#AA(A0)

#for k in A0:
#  A0[k] = 4
visited[frozenset(A0.items())] = 0
k_A0 = frozenset(A0.items())

for ii in range(1000000):
  L = list(visited)
  x = random.choice(L)
  if ii % 1000 == 0:
    print ii, len(visited)
  search(dict(x), visited[x])

print len(visited)
for k in sorted(visited, key=score)[:10]:
  print score(k), visited[k], k
print best


"""



def f(A):
  src = A['E']

  i = 0
  while i < 1000:
    src_parts = [k for (k,v) in A.iteritems() if v == src and k != 'E']
    dst = random.choice(list(set([1,2,3,4]) & set([src + 1, src - 1])))
    choices = list(itertools.combinations(src_parts, 1))
    choices += list(itertools.combinations(src_parts, 2))
    parts = random.choice(choices)

    if isSafe(A, src, dst, parts):
      return move(A, dst, parts)
      break
    else:
      i += 1
  if i > 999:
    assert False, A


#A = dict(A0)
#print A
#move(2, ['HM'])
#print A
#print isDstSafe(1, ['HG', 'HM'])
#move(1, ['HG', 'HM'])
#print A


from collections import Counter
from collections import defaultdict

A = None
def g():
  global A
  states = dict()
  for j in range(100000):
    if j < 1000:
      A = dict(A0)
      ii=0
    else:

      kf = lambda kk: sum(y for (x,y) in kk)
      #a = (random.choice(sorted(states.keys(),key=kf)[-20:]))
      a = (random.choice(states.keys()))
      A = dict(a)
      ii=states[a]
    for i in range(ii,38):
      st = f(A)
      st = tuple(sorted(st.items()))
      if st not in states:
        states[st] = i+1
      elif states[st] < i+1:
        break
      else:
        states[st] = i+1

  return states

#print f(A)

states = g()

kf = lambda kk: sum(y for (x,y) in kk)
for k, grp in itertools.groupby(sorted(states, key=kf),key=kf):
  x = grp.next()
  print k, states[x], x
"""
