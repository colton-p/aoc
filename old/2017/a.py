import itertools


def eval(tree):
  if tree.__class__ != Op:
    return tree

  l = eval(tree.left)
  r = eval(tree.right)

  return tree.op(l, r)

def pp(tree):
  if tree.__class__ != Op:
    return str(tree)

  l = pp(tree.left)
  r = pp(tree.right)

  return '(%s %s %s)' % (l, tree.op.__name__, r)


class Op:
  def __init__(self, op, left, right):
    self.left = left
    self.right = right
    self.op = op

  def __str__(self):
    return pp(self)



def gen_trees(ll, ops):
  assert len(ll)  == len(ops) + 1, (ll, ops)
  if len(ll) == 1:
    return ll
  elif len(ll) == 2:
    return [Op(ops[0], ll[0], ll[1])]

  r = []
  for i in range(1,len(ll)):
    ll_l,ll_r = ll[:i], ll[i:]
    ops_l, ops_r = ops[1:i], ops[i:]

    for (left, right) in itertools.product(gen_trees(ll_l, ops_l), gen_trees(ll_r, ops_r)):
      r += [Op(ops[0], left, right)]

  return r

def concat(x,y):
  return int(str(x) + str(y))

def div(x,y):
  if y == 0:
    raise ValueError
  if x % y == 0:
    return x / y
  else:
    raise ValueError

import operator
OPS = [operator.add, operator.sub, operator.mul, div]


def all_ops(n):
  return itertools.product(*[OPS for i in range(n)])



def f(num):
  c = 0
  for ops in all_ops(len(num)-2):
    L = gen_trees(num, [operator.eq] + list(ops))
    for t in L:

      try:
        rslt = eval(t)
        if rslt == True:
          return t
      except ValueError:
        pass
  return False

N = 7

for num in itertools.product([1,2,3,4,5,6,7,8,9],*[range(1,10) for i in range(N-1)]):
  print num
  if not f(num):
    print num
    break




