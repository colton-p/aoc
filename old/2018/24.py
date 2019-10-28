#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 24'
print '------'

rows = input_rows('24', test=False)

print 'row count:', len(rows)
print '------'

class Group:
  is_targetted = None
  target = None
  def __init__(self, team, ll):
    (n_units, hp, damage, init,dmg_type, weak, immune) = ll
    self.team=team
    self.n_units = n_units
    self.hp = hp
    self.damage =damage
    self.init = init
    self.dmg_type = dmg_type
    self.weak  = weak
    self.immune = immune

  def __str__(self):
    return '%s(n=%d hp=%d dmg=%d(%s) init=%d weak=%s imm=%s)'%(self.team, self.n_units,self.hp,self.damage,self.dmg_type,self.init,self.weak,self.immune)


  def effective_power(self):
    assert self.n_units > 0
    return self.n_units * self.damage

  def damage_dealt(self, target):
    assert self.n_units > 0
    assert target.n_units > 0
    base = self.effective_power()

    if self.dmg_type in target.weak:
      return base * 2
    if self.dmg_type in target.immune:
      return 0

    return base

  def receive_damage(self, damage):
    assert self.n_units > 0
    assert damage > 0
    self.n_units -= (damage / self.hp)


def build_game():
  G = []
  for row in rows:
    ll = extract_numbers(row)
    if not ll:
      if row:
        team = row[:-1]
      continue

    (n_units, hp, damage, init) = ll
    m = re.search('(\w+) damage', row)
    dmg_type = m.group(1)

    weak = []
    immune = []
    m = re.search('\((.*)\)', row)
    if m:
      mods = m.group(1)

      o_mods = mods
      mods = (mods.split(';'))
      for mod in mods:
        m = re.search('weak to (.*)', mod)
        if m:
          weak += m.group(1).split(', ')
        m = re.search('immune to (.*)', mod)
        if m:
          immune += m.group(1).split(', ')

    G += [Group(team, (n_units, hp, damage, init,dmg_type, weak, immune))]
  return G


ORIG_G = build_game()

def targetting_order(groups):
  def sort_key(grp):
    return (-grp.effective_power(), -grp.init)

  return sorted(groups, key=sort_key)


def attacking_order(groups):
  def sort_key(grp):
    return -grp.init

  return sorted(groups, key=sort_key)




def select_target(group, G):
  def sort_key(target):
    return (group.damage_dealt(target), target.effective_power(), target.init)

  targets = [tgt for tgt in G if group.team != tgt.team and tgt.is_targetted is None and group.damage_dealt(tgt) != 0]
  if not targets:
    return None

  print ''
  for t in sorted(targets, key=sort_key, reverse=True):
    print sort_key(t), str(t)
  print ''

  return max(targets,key=sort_key)


def fight(G):

  for g in targetting_order(G):
    assert g.n_units > 0
    tgt = select_target(g, G)
    if tgt:
      assert g.target is None
      assert tgt.is_targetted is None
      assert tgt.n_units > 0
      g.target = tgt
      tgt.is_targetted = g

  for g in attacking_order(G):
    if g.n_units <= 0:
      continue
    tgt = g.target
    if tgt:
      assert tgt.is_targetted == g
      assert tgt.n_units > 0

      dmg = g.damage_dealt(tgt)
      print 'dmg', dmg
      assert dmg > 0
      #print '%d attacks %d: %d damage' % (g.init, tgt.init, dmg)
      tgt.receive_damage(dmg)

  for g in G:
    g.target = None
    g.is_targetted = None

  return [g for g in G if g.n_units > 0]



def go(G, boost):
  for g in G:
    if g.team == 'Immune System':
      g.damage += boost

  while True:
    G = fight(G)

    print '------'
    for g in G:
      print str(g)
    print '------'

    if len([g for g in G if g.team == 'Immune System']) in [0, len(G)]:
      break
    print sum([g.n_units for g in G if g.team == 'Immune System']), sum([g.n_units for g in G if g.team == 'Infection'])

  #print '---'
  #for g in G:
  #  print str(g)

  return G[0].team, sum([g.n_units for g in G])

import sys
print go(build_game(), int(sys.argv[1]))
