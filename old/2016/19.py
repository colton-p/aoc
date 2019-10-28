import sys 
N = 3001330
N = int(sys.argv[1])
L = [i+1 for i in range(N)]

"""
while len(L) > 1:
  i = 0
  to_keep = []
  while i < len(L):
    to_keep.append(L[i])
    i += 2
  if i == len(L) + 1:
    to_keep.pop(0)
  L = to_keep
  if len(L) < 20:
    print L
  else:
    print len(L)
"""

from collections import deque
L = deque(L)

while len(L) > 1:
  i = 0
  to_keep = []
  
  k =(len(L)+1)/2
  L.rotate(k)
  x = L.popleft()
  L.rotate(-k)

  if len(L) % 1 == -1:
    if len(L) < 20:
      print x, L
    else:
      print len(L)

import math
def f(n):
  k = int(math.log(n-1,3))
  
  a = 3**k
  b = 3**(k+1)
  z = b - a

  d = n-a

  if d < a:
    return d
  else:
    return 2*d - a #(a) + 2*(n-2*a)


print L[0], f(N)
