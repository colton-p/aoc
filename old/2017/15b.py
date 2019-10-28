def gA_1(x):
  while True:
    x = (x * 16807) % 2147483647
    yield x

def gB_1(x):
  while True:
    x = (x * 48271) % 2147483647
    yield x

def gA_2(x):
  while True:
    x = (x * 16807) % 2147483647
    if x % 4 == 0:
      yield x

def gB_2(x):
  while True:
    x = (x * 48271) % 2147483647
    if x % 8 == 0:
      yield x

a = 512
b = 191
c = 0

gA = gA_2(a)
gB = gB_2(b)

for i in xrange(5*1000*1000):
  a = next(gA)
  b = next(gB)

  if (a & 65535) == (b & 65535):
    c += 1

print c


