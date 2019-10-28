import re

import hashlib



#def H(x):
  #key = 'abc'
#  key = 'ahsbgdzn'
#  return hashlib.md5(key+str(x)).hexdigest()

def H(x):
  #key = 'abc'
  key = 'ahsbgdzn'
  a = hashlib.md5(key+str(x)).hexdigest()
  for i in range(2016):
    a = hashlib.md5(a).hexdigest()
  return a


def triple(x):
  m = re.search('(.)\\1\\1', x)
  if m:
    return m.group(1)

def five(x, c):
  return (c*5) in x


L = []
for i in range(0, 1001):
  L += [H(i)]

i = 0
c = 0
while c != 64:
  assert len(L) == 1001
  x = L.pop(0)
  #assert x == H(i), i
  s = triple(x)
  if s:
    assert len(L) == 1000
    if any(five(y, s) for y in L):
      c += 1
      print c, i#, H(i)
  i+= 1
  L.append(H(i+1000));
