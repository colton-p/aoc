#coding=utf-8
VV = 1358

def bits(v):
  c = 0
  while v:
    v &= (v-1)
    c+=1
  return c

def n(x,y):
  n = x*x + 3*x +2*x*y + y +y*y + VV
  v = bits(n)
  return v % 2 == 0




def adj(x, y):
  for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
      if i !=0 and j !=0:
        continue
      if i!=j and n(x+i, y+j) and x+i >= 0 and y+j >=0:
        yield (x+i, y+j)


pr = {}
visited = {}
to_visit = [(0, (1,1))]
while to_visit:
  d, pt = to_visit.pop(0)

  visited[pt] = d

  #if pt == (31,39):
  #if pt == (7,4):
 #   print '!!!', d
  #  break
  if d == 50:
    continue

  to_add = [(d+1, p) for p in adj(*pt) if p not in visited]
  for (_,p) in to_add:
    pr[p] = pt
  to_visit.extend(to_add)

L = []
p = (31,39)
while p in pr:
  L += [p]
  p = pr[p]
print L


for y in range(50):
  line = ''
  for x in range(50):
    if (x,y) == (1,1):
      line += 'O '
    elif (x,y) == (31,39):
      line += 'X '
    elif (x,y) in visited:
      line += '. '
    else:
      line += ('  ' if n(x,y) else '🁢 ')
  print line


