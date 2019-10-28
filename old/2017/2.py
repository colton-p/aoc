
import fractions


f = open('2.in', 'r')

l = []
for i in f:
  l += [map(int, i.strip().split('\t'))]


print sum([max(ll) - min(ll) for ll in l])




s = 0
for ll in l:
  for x in ll:
    for y in ll:
      r = y % x
      if y > x and r == 0:
        s += y/x
print s

print ''
import itertools

print sum( max(line) - min(line) for line in l)
print sum( y/x for line in l for (x,y) in itertools.combinations(sorted(line), 2) if y % x == 0 )
