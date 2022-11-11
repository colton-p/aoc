from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output
import dataclasses

YEAR = 2021
DAY = 16

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def build_value_bits(it):
  ind = True
  val = ''
  nbits = 0
  while ind != '0':
    ind = next(it)
    val_bits = itertools.islice(it, 4)
    val += ''.join(val_bits)
    nbits += 5
  
  return val, nbits

def build_packet(it, depth=0):
  nbits = 6
  ver_bits = next(it), next(it), next(it)
  version = int(''.join(ver_bits), 2)

  type_bits = next(it), next(it), next(it)
  type = int(''.join(type_bits), 2)
  if type == 4:
    value_bits, n_value_bits = build_value_bits(it)
    nbits += n_value_bits
    value = int(value_bits, 2)

    return Packet(version, type, [], value, nbits=nbits)
  
  length_type_id = int(next(it))
  nbits += 1

  children = []
  if length_type_id == 0:
    n_subbits = int(''.join(itertools.islice(it, 15)), 2)
    nbits += n_subbits
    nbits += 15

    while n_subbits > 0:
      subpacket = build_packet(it, depth + 1)
      children += [subpacket]
      n_subbits -= subpacket.nbits
    
    assert n_subbits == 0
    return Packet(version, type, children, None, nbits=nbits)

  elif length_type_id == 1:
    n_subpackets = int(''.join(itertools.islice(it, 11)),2)
    nbits += 11

    children = [build_packet(it, depth+1) for i in range(n_subpackets)]
    nbits += sum(p.nbits for p in children)

    return Packet(version, type, children, None, nbits=nbits)

@dataclasses.dataclass(frozen=True)
class Packet:
  version: int
  type: int
  children: list
  value: int
  nbits: int

  def pretty(self, depth=0):
    padding = '..' * depth
    print(f'{depth} {padding} v={self.version} t={self.type} nbits={self.nbits} val={self.value} {self.evaluate()}')

    for c in self.children:
      c.pretty(depth+1)
  
  def version_sum(self):
    return self.version + sum(c.version_sum() for c in self.children)
  
  def evaluate(self):
    if self.value is not None:
      return self.value
    
    subvals = [c.evaluate() for c in self.children]
    nary = { 0: sum, 1: prod, 2: min, 3: max }
    binary = { 5: op.gt, 6: op.lt, 7: op.eq }

    if self.type in nary:
      return nary[self.type](subvals)

    if self.type in binary:
      assert len(self.children) == 2
      return binary[self.type](*subvals)

def part1(rows, iobj):
  #ss = '8A004A801A8002F478'
  #ss = '620080001611562C8802118E34'
  #ss = 'C0015000016115A2E0802F182340'
  ss = 'A0016C880162017C3686B18A3D4780'
  raw = bin(int('F'+ss, 16))[6:]
  print(len(raw))


  for x in parse1(iter(raw)):
    print('-->', x)

  return sum(x[0] for x in parse1(iter(raw)))

def part2(rows, iobj):

  #ss = 'D2FE28'
  #ss = '38006F45291200'
  #ss = 'EE00D40C823060'
  #ss = '8A004A801A8002F478'
  #ss = '620080001611562C8802118E34'
  #ss = 'C0015000016115A2E0802F182340'
  #ss = 'A0016C880162017C3686B18A3D4780'
  #ss = 'C200B40A82'
  #ss = '9C0141080250320F1802104A08'


  raw = bin(int('F'+ss, 16))[6:]


  print('raw len', len(raw))
  it = iter(raw)
  packet = build_packet(it)
  print(packet)

  rem = [r for r in it]
  assert len(raw) == len(rem) + packet.nbits
  assert all([r == '0' for r in rem])
  
  packet.pretty()


  return packet.evaluate()

#util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
