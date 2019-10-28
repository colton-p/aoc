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
'ElG': 1, 'ElM': 1, 'DiG': 1, 'DiM': 1,
'E': 1
}

def canonical(A):
  B = dict(A)
  kk = sorted(['ThG', 'PuG', 'ElG', 'DiG'])
  vv = sorted(kk, key=lambda x: A[x])

  for (k,v) in zip(kk, vv):
    B[k] = A[v]

  kk = sorted(['ThM', 'PuM', 'ElM', 'DiM'])
  vv = sorted(kk, key=lambda x: A[x])

  for (k,v) in zip(kk, vv):
    B[k] = A[v]
  return B

An = dict(A0)
for k in An:
  An[k] = 4


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
        yield canonical(move(state, dst, parts))


class Object(object):
  pass

def search(score):
  scope = Object()
  scope.best = (None, 10000, 100000)
  scope.visited = dict()
  def visit(state, depth):
    k_state = frozenset(state.items())

    if k_state in scope.visited and scope.visited[k_state] < depth:
      depth = scope.visited[k_state]
      return
    else:
      scope.visited[k_state] = depth

    if depth + scope.visited[k_state] > 97:
      return

    if (score(state.items()), depth) < (scope.best[1], scope.best[2]):
      scope.best = (frozenset(state.items()), score(state.items()), depth)
      #print '*', scope.best
      if score == fwd_score:
        print 'fwd', scope.best[1], '(%d)' % scope.best[2]
      else:
        print 'rev', fwd_score(scope.best[0]), '(%d)' % scope.best[2]


    l = list(adj(state))
    if not l:
      return
    new_state = random.choice(list(adj(state)))
    visit(new_state, depth+1)

  return visit, scope


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



fwd_score = lambda kk: 56 - sum(flr if obj != 'E' else 0 for (obj,flr) in kk)
rev_score = lambda kk: sum(flr if obj != 'E' else 0 for (obj,flr) in kk)
fwd, fwd_scope = search(fwd_score)
rev, rev_scope = search(rev_score)

fwd(A0, 0)
rev(An, 0)
for ii in range(4000):
  fwd_x = random.choice(list(fwd_scope.visited))
  fwd(dict(fwd_x), fwd_scope.visited[fwd_x])

  rev_x = random.choice(list(rev_scope.visited))
  rev(dict(rev_x), rev_scope.visited[rev_x])

  if ii % 1000 == 0:
    print ii, len(fwd_scope.visited), len(rev_scope.visited)


print '---'
print 'v', fwd_scope.best[1]
print '^', fwd_score(rev_scope.best[0])

print '---'
S = set(fwd_scope.visited.keys()) & set(rev_scope.visited.keys())
print len(fwd_scope.visited), len(rev_scope.visited)
print len(S)

for k in S:
  print fwd_scope.visited[k] + rev_scope.visited[k], k




