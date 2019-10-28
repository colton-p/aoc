from util import *
with open('2015-24.in', 'r') as f:
  nums = [int(line.strip()) for line in f]


print(sum(nums))

# nums = [1,2,3,4,5,7,8,9,10,11]

def f(nums):
  s = set(nums)
  tgt = sum(s) / 4
  for t1 in powerset(s):
    s1 = set(t1)

    if sum(s1) != tgt:
      continue
    for t2 in powerset(s - s1):
      s2 = set(t2)
      if sum(s2) != tgt:
        continue
      for t3 in powerset(s - s1 - s2):
        s3 = set(t3)
        if sum(s3) != tgt:
          continue

        yield (s1, s2, s3, s - s1-s2-s3)

# for x in sorted(f(nums), key=lambda x: [len(x[0]), product(x[0])])[:1]:
v, qe = len(nums), product(nums)
for x in f(nums):
  if (len(x[0]), product(x[0])) < (v,qe):
    v,qe = len(x[0]), product(x[0])
    print("*****", v, qe)

print('*****>', v,qe)
