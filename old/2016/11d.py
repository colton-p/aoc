import itertools
import collections

from ts import total_size as ts

ATest = {
  'HM': 1,
  'HG': 2,
  'LM': 1,
  'LG': 3,
  'E':  1
}

A0 = {
'AG': 3, 'AM': 3, 'BG': 3, 'BM': 3,
'CM': 2, 'DM': 2,
'EG': 1, 'EM': 1, 'CG': 1, 'DG': 1,
#'FG': 1, 'FM': 1, 'GG': 1, 'GM': 1,
'E': 1
}



KEYS = sorted(A0.keys())
def freeze(A):
  return int(''.join([str(A[k]) for k in KEYS]))

def thaw(A):
  return dict([(k,int(v)) for k, v in zip(KEYS, str(A))])

#assert freeze(thaw(freeze(A0))) == freeze(A0)

A0 = (1, (
  (1,1), (1,1),
  (1,1), (1,2),
  (1,2),
  (3, 3), (3,3)),

  frozenset([1,2,3]),
  frozenset([2])
  )
#def canonical(A):
#  B = dict(A)
#  kk = sorted(['ThG', 'PuG', 'ElG', 'DiG'])
#  vv = sorted(kk, key=lambda x: A[x])
#
#  for (k,v) in zip(kk, vv):
#    B[k] = A[v]
#
#  kk = sorted(['ThM', 'PuM', 'ElM', 'DiM'])
#  vv = sorted(kk, key=lambda x: A[x])
#
#  for (k,v) in zip(kk, vv):
#    B[k] = A[v]
#  return B

#An = dict(A0)
#for k in An:
#  An[k] = 4

def isSrcSafe(A, floor, parts):
  src_gens  = [k for (k,v) in A.iteritems() if v == floor and k[-1] == 'G' and k not in parts]
  src_chips = [k for (k,v) in A.iteritems() if v == floor and k[-1] == 'M' and k not in parts]

  if not src_gens:
    return True

  return all([((chip[:-1]+'G') in src_gens) for chip in src_chips])

def isDstSafe(A, floor, parts):
  dst_parts = [k for (k,v) in A.iteritems() if v == floor and k != 'E'] + list(parts)
  dst_gens = [k for k in dst_parts if k[-1] == 'G']
  dst_chips = [k for k in dst_parts if k[-1] == 'M']

  if not dst_gens:
    return True

  return all([((chip[:-1]+'G') in dst_gens) for chip in dst_chips])

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


def move(state, ixs, new_floor):
  (floor, pairs, gens, unpaired) = state
  pairs = list(pairs)

  for (i,j) in ixs:
    if j == 0:
      pairs[i] = (new_floor, pairs[i][1])
    else:
      pairs[i] = (pairs[i][0], new_floor)

  gens = frozenset([pp[1] for pp in pairs])
  unpaired = frozenset([pp[0] for pp in pairs if pp[0] != pp[1]])

  '''
  gens = set()
  unpaired = set()
  for (i,j) in pairs:
    gens.add(j)
    if i != j:
      unpaired.add(i)
  '''

  pairs.sort()
  return (new_floor, tuple(pairs), gens, unpaired)

def move(state, ixs, new_floor):

  new_pairs = []
  for (i,j) in pairs:
    if j == 0:
      pairs[i] = (new_floor, pairs[i][1])
    else:
      pairs[i] = (pairs[i][0], new_floor)


def isSafe(state, o_floor):
  (floor, pairs, gens, unpaired) = state


  if unpaired & gens:
    return False
  else:
    return True

  '''
  for fl in (o_floor, floor):
    chips, gens = False, False
    for (x,y) in pairs:
      if y == fl:
        chips = True
      elif y != fl and x == fl:
        gens = True
      if chips and gens:
        return False
  return True
  '''

OPTS = list(itertools.product(range(len(A0[1])), [0,1]))

FLOOR_OPTS = {
1:  (2,),
2:  (1,3),
3:  (2,4),
4:  (3,),
}


def adj(state):
  (floor, pairs, gens, unpaired) = state

  x = [(i,j) for (i,j) in OPTS if pairs[i][j] == floor]
  choices = [(o,) for o in x]
  choices += list(itertools.combinations(x, 2))

  for new_floor in FLOOR_OPTS[floor]:
    for ixs in choices:
      new_state = move(state, ixs, new_floor)

      if isSafe(new_state, floor):
        yield new_state


class Object(object):
  pass

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

def search(start, score):
  visited = 0
  to_visit = collections.deque([ start ])
  distance = {}
  distance[start] = 0
  best = (start, score(start), 0)

  last_depth = None

  #print '%3s %7s %7s %7s | %s' % ('d', 'visited', 'seen', 'to_vst', 'best score depth')
  while to_visit:
    state = to_visit.popleft()
    depth = distance[state]
    visited += 1

    #if depth != last_depth:
    #  last_depth = depth
    #  print '%3d %7d %7d %7d | %s' % (depth, visited, len(distance), len(to_visit), str(best))

    #if ( (score(state), depth) < (best[1], best[2])):
    # best = (state, score(state), depth)
    # #print '*', best
    if state[1] == ((4, 4), (4, 4), (4, 4), (4, 4), (4, 4), (4, 4), (4, 4)):
      print depth

    for s in adj(state):
      if s not in distance:
        distance[s] = depth + 1
        to_visit.append(s)


fwd_score = lambda kk: 60 - sum([sum(x) for x in kk[1]])
#rev_score = lambda kk: sum(flr if obj != 'E' else 0 for (obj,flr) in kk)

#fwd_score = lambda state: 60 - sum(thaw(state).values())


search(A0, score=fwd_score)
