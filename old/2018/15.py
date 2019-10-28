#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

class Actor:
  def is_foe(self, other):
    if isinstance(other, str): return False

    return self.__class__ != other.__class__


class Goblin(Actor):
  dead = False
  def __init__(self, pt):
    self.pt = pt
    self.power = 3
    self.hp = 200
  def __str__(self):
    return 'G'


class Elf(Actor):
  dead = False
  def __init__(self, pt, power):
    self.pt = pt
    self.power = power
    self.hp = 200
  def __str__(self):
    return 'E'




def print_grid(G):
  max_x = max(G.keys(), key=lambda x:x[0])[0]
  max_y = max(G.keys(), key=lambda x:x[1])[1]

  min_x = min(G.keys(), key=lambda x:x[0])[0]
  min_y = min(G.keys(), key=lambda x:x[1])[1]

  print '   '+''.join(['%1d' % (x/10) for x in range(min_x, max_x)])
  print '   '+''.join(['%1d' % (x%10) for x in range(min_x, max_x)])
  for y in range(min_y, max_y+1):
    line = '%2d ' % y
    for x in range(min_x, max_x+1):
      line += (str(G[(x,y)]).strip())
    line += ' | '
    for x in range(min_x, max_x+1):
      if isinstance(G[(x,y)], str):
        continue
      line += '%s(%3d) ' %(G[(x,y)], G[(x,y)].hp)
    print line

def build_grid(power):
  rows = input_rows('15', test=False, strip=False)
  G = {}
  for (y,row) in enumerate(rows):
    for (x,val) in enumerate(row):
      if val == 'E':
        val = Elf((x,y), power)
      elif val == 'G':
        val = Goblin((x,y))
      G[(x,y)] = val
  return G

def all_actors():
  def sort_key(actor):
    return (actor.pt[1], actor.pt[0])
  return sorted([v for v in G.values() if not isinstance(v, str)], key=sort_key)

def reading_order_key(actor):
  (x,y) = actor.pt
  return (y, x)

def targets_for(actor):
  targets = [val for val in G.values() if actor.is_foe(val)]
  return sorted(targets, key=reading_order_key)

def open_in_range_for(target):
  return [(x,y) for (x,y) in rect_adj(target.pt) if G[(x,y)] == '.']

def adjacent_fn(pt):
  return [(x,y) for (x,y) in rect_adj(pt) if G[(x,y)] == '.']

def shortest_distance(src, dst):
  path = bfs(start=src, adjacent_fn=adjacent_fn, goal_fn=lambda x: x==dst)
  if path:
    return len(path) - 1
  else:
    return 9999999


def chose_destination(actor):
  targets = targets_for(actor)
  if not targets:
    raise
  all_destinations = list(itertools.chain(*[open_in_range_for(target) for target in targets]))
  all_destinations = [x for x in all_destinations if shortest_distance(actor.pt, x) < 9999999]
  if not all_destinations: return None


  def sort_key(dst):
    return ( shortest_distance(actor.pt, dst), (dst[1], dst[0]) )

  #for dst in sorted(all_destinations, key=sort_key):
  #  print dst, shortest_distance((2,1), dst)

  return min(all_destinations, key=sort_key)

def chose_first_step(actor, destination):
  def sort_key(src):
    return ( shortest_distance(src, destination), (src[1], src[0]) )

  first_steps = adjacent_fn(actor.pt)
  #for first_step in first_steps:
  #  print first_step, shortest_distance(first_step, destination)
  first_steps = [x for x in first_steps if shortest_distance(x, destination) < 9999999]

  if not first_steps:
    return

  return min(first_steps, key=sort_key)

def check_grid():
  for (k,v) in G.iteritems():
    if not isinstance(v, str):
      assert v.pt == k

class DeadElf:
  pass

def attack(actor):
  if actor.dead:
    return
  def sort_key(enemy):
    return (enemy.hp, (enemy.pt[1], enemy.pt[0]))

  enemies = [ G[pt] for pt in rect_adj(actor.pt) if actor.is_foe(G[pt]) ]
  if not enemies:
    return False

  #for enemy in enemies:
  #  print enemy.pt, enemy.hp

  foe = min(enemies,key=sort_key)

  foe.hp -= actor.power
  if foe.hp <= 0:
    foe.dead = True
    G[foe.pt] = '.'
    if str(foe) == 'E':
      raise DeadElf

  return True


def move(actor):
  if actor.dead:
    return

  destination = chose_destination(actor)
  if not destination: return
  step = chose_first_step(actor, destination)
  if not step: return

  assert G[step] == '.'

  G[actor.pt] = '.'
  G[step] = actor
  actor.pt = step
  check_grid()


G = {}
def play(power=3):
  global G
  G = build_grid(power)
  #print_grid(G)


  #print ''
  try:
    for i in range(1, 1000):
      for actor in all_actors():
        if not targets_for(actor):
          rounds = i-1
          hp = sum(a.hp for a in all_actors())
          score = rounds * hp
          print_grid(G)
          print '%d * %d = %d' % (rounds, hp, score)
          return (str(all_actors()[0]), rounds, hp, score)
          exit()

        if not attack(actor):
          move(actor)
          attack(actor)
      #print 'After %d rounds: ' % i
      #print_grid(G)
  except DeadElf:
    print_grid(G)
    return ('G', i)

for i in range(39, 100):
  rslt = play(i)
  print i, rslt
  if rslt and rslt[0] == 'E':
    break
