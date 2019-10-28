import operator

Ltest = [
(4, 5),  # (x + 4) + 1 == 0 mod 5     x == 0 mod 5
(1, 2)  # (x + 1) + 2 == 0 mod 2 --> x+1 == 0 mod2
]

L  = [
(11, 13),
(0,  5 ),
(11, 17),
(0,  3 ),
(2,  7 ),
(17, 19),
(0, 11)
]



def inv(x,m):
  x = x % m
  for i in range(m):
    if (x*i) % m == 1:
      return i
  print x,m


#L = [(1, 5), (2,7), (3,9), (4,11)]

def process(L):
  for (i, (a, m)) in enumerate(L):
    yield  ( m - (a+(i+1) % m), m )




def crt(L):
  a = [ai for (ai,mi) in L]
  m = [mi for (ai,mi) in L]

  MM = reduce(operator.mul, m)
  M = [MM/mi for mi in m]
  y = [inv(Mi, mi) for (Mi, mi) in zip(M, m)]
  x = sum([ai*Mi*yi % MM for (ai, Mi, yi) in zip(a, M, y)]) % MM
  return x


print list(process(L))
print crt(list(process(L)))
