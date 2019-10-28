import collections

def read():
  with open('24.in.txt', 'r') as f:
    return set([tuple(map(int, line.split('/'))) for line in f])

pairs = read()

print pairs


def connector(path):
  if len(path) == 0:
    return 0
  if len(path) == 1:
    a = [0]
    b = path[-1]
  else:
    (a,b) = path[-2:]

  if b[0] in a:
    conn = b[1]
  elif b[1] in a:
    conn = b[0]
  else:
    assert False, (a,b)
  return conn

def adj(path):
  conn = connector(path)
  available = pairs - set(path)
  return set([pt for pt in available if conn in pt])

def score(path):
  return sum(map(sum,path))


L = collections.deque([[]])

DONE = []
m = (None, 0, 0)

while len(L) > 0:
  path = L.popleft()
  nn = adj(path)
  for n in nn:
    L.append(path + [n])
  if not nn:
    if len(path) > m[1]:
      m = (path, len(path), score(path))
    elif len(path) == m[1] and score(path) > m[2]:
      m = (path, len(path), score(path))
    #m = max([m, (path, len(path), score(path))], key=lambda x: (x[1], x[2]))

print len(DONE)
print len(L)

print ''
#m = max(DONE, key=lambda x: (len(x), score(x)))
print m
#print len(m)
#print score(m)
