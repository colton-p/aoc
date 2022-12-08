import collections
import itertools
import math
import random
import operator
import fractions


PRIMES_1K = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])

def is_prime(n):
  """
  >>> is_prime(2)
  True
  >>> is_prime(101)
  True
  >>> is_prime(1009 * 1013)
  False
  >>> is_prime(2**31 - 1)
  True
  """

  if n <= 1000:
    return n in PRIMES_1K

  if n <= 1:
    return False
  if n <= 3:
    return True

  if n % 2 == 0 or n % 3 == 0:
    return False

  k = math.ceil(math.sqrt(n))
  i = 5
  while i <= k:
    # 6k - 1 or 6k + 1
    if n % i == 0 or n % (i+2) == 0:
      return False
    i += 6
  return True

def is_prime_prob(n, k = 5):
  """ Miller-Rabin test, checking k different bases
  >>> is_prime_prob(101)
  True
  >>> is_prime_prob(2**61 - 1)
  True
  """
  if n <= 1000:
    return is_prime(n)
  if n % 2 == 0:
    return False

  r = 0
  d = n - 1
  while d % 2 == 0:
    r += 1
    d //= 2
  assert d * (2**r) == n - 1, (r, d)

  for ki in range(k):
    a = random.randint(2, n - 2)
    x = pow(a, d, n)

    if x == 1 or x == n-1:
      continue

    for ri in range(r-1):
      x = pow(x, 2, n)
      if x == 1:
        return False
      if x == n - 1:
        break
    if x != n - 1:
      return False
  return True


def trial_divisors():
  for p in PRIMES_1K:
    yield p
  i = 1001
  while True:
    yield i       # 6k - 1
    yield i + 2   # 6k + 1
    i += 6


def prime_factors(n):
  """
  >>> prime_factors(48)
  {2: 4, 3: 1}
  """
  ret = collections.defaultdict(int)
  for d in trial_divisors():
    if n <= 1:
      break
    while n % d == 0:
      n //= d
      ret[d] += 1
  return dict(ret)

def integer_factors(n):
  """
  >>> integer_factors(13)
  [1, 13]
  >>> integer_factors(48)
  [1, 2, 3, 4, 6, 8, 12, 16, 24, 48]
  """

  def powerset(iterable):
    """
    >>> list(powerset([1,2,3]))
    [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))
  ps = prime_factors(n)
  ps = itertools.chain(*[ itertools.repeat(k,v) for (k,v) in ps.items()])

  return sorted(list(set(prod(s) for s in powerset(ps))))


def prod(iterable):
  """
  >>> prod([1,2,3,4])
  24
  """
  return math.prod(iterable)

def gcd(a,b):
  """
  >>> gcd(12, 8)
  4
  >>> gcd(7, 3)
  1
  """
  return math.gcd(a, b)

def gcdex(a, b):
  """
  (g, s, t, u, v) = gcdex(a, b)
  g == (s * a) + (t * b)
  0 == (u * a) + (v * b)

  >>> gcdex(12, 8)
  (4, 1, -1, -2, 3)
  >>> gcdex(5, 3)
  (1, -1, 2, 3, -5)
  """
  (old_s, old_t, old_r) = (1, 0, a)
  (s, t, r) = (0, 1, b)
  while r != 0:
    q = old_r // r
    (old_r, r) = (r, old_r - q * r)
    (old_s, s) = (s, old_s - q * s)
    (old_t, t) = (t, old_t - q * t)

  (g, s, t, u, v) = (old_r, old_s, old_t, s, t)
  return (g, s, t, u, v)

def modinv(x, n):
  """
  >>> modinv(7, 10)
  3
  >>> modinv(4, 10)
  Traceback (most recent call last):
    ...
  ZeroDivisionError: (4, 10)
  """
  (g, s, t, u, v) = gcdex(x, n)
  if g != 1:
    raise ZeroDivisionError(x, n)

  return s % n


def simul_congruence(n, a):
  """
  solve { x = a_i mod n_i }
  """
  NN = prod(n)
  N = [NN // ni for ni in n]
  M = [modinv(Ni, ni) for (Ni, ni) in zip(N, n)]

  return sum(ai * Mi * Ni for (ai, Mi, Ni) in zip(a, M, N)) % NN

def binom(n, k):
  """
  >>> binom(4, 2)
  6
  >>> binom(9, 4)
  126
  """
  return math.comb(n, k)

if __name__ == '__main__':
  import doctest
  doctest.testmod()


