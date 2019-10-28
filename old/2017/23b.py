a = b = c = d = e = f = g = h = 0
a = 1

print '%8s | %4s %4s %4s %4s %4s %4s %4s %4s' % ('', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
def pp(lbl =''):
  print '%8s | %4d %4d %4d %4d %4d %4d %4d %4d' % (lbl, a, b, c, d, e, f, g, h)


b = 65
c = 65
#import sys
#b = int(sys.argv[1])
#k = int(sys.argv[2])

#c = b + k*17

import num_util
if a != 0:
  b *= 100
  b += 100000
  c = b
  c += 17000

print b, c
R = xrange(b, c+1, 17)
print sum(1 for x in R if not num_util.is_prime(x))

#pp('init')
while True:
  f = 1

  d = 2
  while True:
    e = 2

    while True:
      if d*e == b:
        f = 0
      e += 1
      if e == b:
        break

    d += 1
    if d == b:
      break

  if f == 0:
    h += 1
  if b == c:
    break
  b += 17


#pp('fini')
print h
