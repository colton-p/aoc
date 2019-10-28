
def overlap(a, b):
  if a[1] +1 >= b[0]:
    return (min(a[0], b[0]), max(a[1], b[1]))
  return None


L = []
inn = ['5-8', '0-2', '4-7']

R = sorted([map(int, line.split('-')) for line in open('20.in', 'r')])

for (a,b) in R:
  assert a < b, (a,b)

for r in R:
  print r

L += [R.pop(0)]

c = 0
while R:
  a = L[-1]
  b = R.pop(0)
  x = overlap(a, b)
  if x:
    L[-1] = x
  else:
    L += [b]
    print a[1], b[0], b[0] - a[1] - 1
    c +=  b[0] - a[1] - 1

print L
print c
