import collections
import itertools
import re
import math
import operator

with open('16.in', 'r') as f:
  rows = [x.strip() for x in f.readlines()]

moves = rows[0].split(',')

def spin(L, x):
  return L[-x:] + L[:-x]

def exchange(L, a, b):
  ll = list(L)
  ll[a], ll[b] =  ll[b], ll[a]
  return ll

def partner(L, x, y):
  ll = list(L)
  a = L.index(x)
  b = L.index(y)
  ll[a], ll[b] =  ll[b], ll[a]
  return ll

L = list('abcdefghijklmnop')

def dance(L, moves):
  for x in moves:
    instr = x[0]
    args = x[1:].split('/')
    if instr == 's':
      L = spin(L, int(args[0]))
    elif instr == 'x':
      L = exchange(L, int(args[0]), int(args[1]))
    elif instr == 'p':
      L = partner(L, (args[0]), (args[1]))

  return L


def dance_generator(state):
  while True:
    state = dance(state, moves)
    yield state





def analyze(gen, s0):
  d = {}
  state = s0
  ll = []

  (cycle_start, cycle_length) = (None, None)

  for i in range(100):
    k = repr(state)
    ll += [k]
    if k not in d:
      d[k] = i
    else:
      (cycle_start, cycle_length) = (d[k], i-d[k])
      break

    #print(i, state)
    state = next(gen)

  return (ll, cycle_start, cycle_length)


def element_at(ix, ll, cycle_start, cycle_length):
  if ix < len(ll):
    return ll[ix]
  else:
    return ll[cycle_start + ((ix  - cycle_start) % cycle_length)]



dance_gen = dance_generator(L)
def repeater():
  yield 1
  yield 2
  yield 3
  yield 4
  yield 5
  while True:
    yield 10
    yield 20
    yield 30
g1 = repeater()


(a,b,c) = analyze(dance_gen, -1)
print(a,b,c)
print(element_at(10**9, a, b, c))


#print(''.join(dance(L, moves)))
