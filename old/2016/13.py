import util
import collections

KEY = 1358


start = (1,1)
goal_fn = lambda s: s == (31, 39)


def adj(s):
  for t in rect_adj(s):
    if not wall(t):
      yield (t, 'x')

def rect_adj(s):
  for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
      if (i,j) != (0,0)
        yield (s[0]+i, s[1]+j)



def wall(s):
  (x,y) = s
  v = x*x + 3*x + 2*x*y + y + y*y + KEY
  #print v
  #print bin(v)
  return collections.Counter(bin(v))['1'] % 2 == 1 or x < 0 or y < 0


print list(rect_adj(start))
print list(adj(start))

print len(util.bfs(start=start, adjacent_fn=adj, goal_fn=goal_fn))

print ''
print wall((7, 0))
print wall((7, 1))
print wall((7, 2))
print wall((7, 3))
