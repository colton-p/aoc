a = 512
b = 191
c = 0

for i in xrange(40*1000*1000):
  a = (a * 16807) % 2147483647
  b = (b * 48271) % 2147483647

  if (a & 65535) == (b & 65535):
    c += 1

print c
