import collections


D = {}
N = {}
for (y,line) in enumerate(open('24.in', 'r')):
  for (x, c) in enumerate(line.strip()):
    D[(x,y)] = c
    try:
      n = int(c)
      N[n] = (x,y)
    except ValueError:
      pass

print N


def adj(D, state):
  (x,y) = state

  if D[(x-1,y)] != '#':
    yield (x-1, y)
  if D[(x+1,y)] != '#':
    yield (x+1, y)
  if D[(x,y-1)] != '#':
    yield (x, y-1)
  if D[(x,y+1)] != '#':
    yield (x, y+1)




def search(D, start, end):

  to_visit = collections.deque([ start ])
  distance = {}
  distance[start] = 0
  pr = {}

  while to_visit:
    state = to_visit.popleft()
    depth = distance[state]

    if (state) == end:
      ret = depth
      break

    for s in adj(D, state):
      if s not in distance:
        distance[s] = depth + 1
        to_visit.append(s)
        pr[s] = state

  L = []
  s = end
  while s in pr:
    L += [s]
    s = pr[s]
  L += [s]

  return L, depth, ret


V = {}

for i in N:
  for j in N:
    if i == j:
      continue
    L, d, e = search(D, N[i], N[j])
    V[(i,j)] = d



def f(l):
  c = 0
  for i in range(len(l)):
    if i == 0:
      c += V[(0, l[i])]
    else:
      c += V[(l[i-1], l[i])]
  c += V[(l[-1], 0)]
  return c

import itertools
it = itertools.permutations([1,2,3,4,5,6,7])
x = min(it, key=f)
print x
print f(x)


it = itertools.permutations([1,2,3,4,5,6,7])
x = max(it, key=f)
print x
print f(x)
#for i in it:
#  print i, f(list(i))


def pp():
  for y in range( max(D, key=lambda x: x[1])[1]):
    for x in range( max(D, key=lambda x: x[0])[0]):
      if (x,y) in N.values():
        print D[(x,y)],
      elif (x,y) in L:
        print '*',
      else:
        print D[(x,y)],
    print ''

