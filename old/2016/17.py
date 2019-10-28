
import hashlib

SIZE = 4

def open_doors(x):
  key = 'mmsxrhfx'
  #key = 'ulqzkmiv'
  h = hashlib.md5(key+x).hexdigest()[:4]
  return [d for (d, c) in zip('UDLR', h) if c in 'bcdef']


DIR = {
'U': (0,-1),
'D': (0,1),
'L': (-1,0),
'R': (1,0),
}

def adj(state, path):
  for door in open_doors(path):
    new = tuple(map(sum, zip(state, DIR[door])))
    if -1 in new or SIZE in new:
      continue

    yield new, path + door

def search():
  visited = 0
  to_visit = [ ((0,0), '') ]
  #distance = {}
  #distance[start] = 0

  last_depth = None
  best = ''

  print '%7s %7s %7s' % ('depth', 'visited', 'to_visit')
  while to_visit:
    (state, path) = to_visit.pop(0)
    depth = len(path)
    visited += 1
    #print visited, state, path

    if state == (SIZE-1,SIZE-1):
      return path, len(path)
      if len(path) > len(best):
        best = path
      continue


    #if depth != last_depth:
    #  last_depth = depth
      #print '%7d %7d %7d | %4d' % (depth, visited, len(to_visit), len(best))

    to_visit.extend(adj(state,path))

  return best, len(best)


x = search()
print ''
print '----------'
print ''
print x
