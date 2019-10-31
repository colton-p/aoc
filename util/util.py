import re
import os

import requests

from itertools import *

def input_rows(day, year=2019, test=False, strip = True):
  path = 'inputs/%s-%s.in' % (year, day)

  if test: path += '.test'

  if not os.path.exists(path):
    print('Fetching new input...')
    input_url = 'https://adventofcode.com/%s/day/%s/input' % (year, day)
    input = requests.get(input_url, cookies={'session': open('.aoc_session').read().strip()}).text
    with open(path, 'w') as f:
      f.write(input)

  with open(path, 'r') as f:
    if strip:
      return [line.strip() for line in f]
    else:
      return [line for line in f]



def input_as_numeric_tuples(day, year=2019):
  rows = input_rows(day, year)

  return [extract_numbers(row) for row in rows]

def input_as_tuples(day, year=2019):
  rows = input_rows(day, year)

  return [
    tuple(safe_int(x) for x in row.split())
    for row in rows
  ]

def input_as_list(day, year=2019):
  rows = input_rows(day, year)
  return [safe_int(x) for x in rows]

def input_as_single_string(day, year=2019):
  (row,) = input_rows(day, year)
  return row

def safe_int(value):
  """
  >>> safe_int('-2')
  -2
  >>> safe_int('xyz')
  'xyz'
  """
  try:
    return int(value)
  except ValueError:
    return value

def analyze_input(rows):
  n_rows = len(rows)
  row_lens = list(map(len, rows))
  kind = "???"

  if n_rows == 1:
    if safe_int(rows[0]) == rows[0]:
      if re.match('^[A-Za-z]+$', rows[0]):
        kind = "string"
      else:
        kind = "one line"
    else:
      kind = "number"
  else:
    if all( [type(safe_int(x)) == int for x in rows]):
      kind = 'list num'

    if len(set(row_lens))==1:
      kind = "grid"

  return (kind, n_rows, max(row_lens), min(row_lens), len(set(row_lens))==1)

def extract_numbers(line):
  """
  >>> extract_numbers('1 -2 3')
  [1, -2, 3]

  >>> extract_numbers('abc-12 - 34')
  [-12, 34]

  >>> extract_numbers('abcdef')
  []
  """
  return [int(x) for x in re.findall('-?\d+', line)]

def pairwise(iterable):
  """s -> (s0,s1), (s1,s2), (s2, s3), ...

  >>> list(pairwise([1, 2, 3, 4]))
  [(1, 2), (2, 3), (3, 4)]
  """
  a, b = tee(iterable)
  next(b, None)
  return zip(a, b)




if __name__ == '__main__':
  import doctest
  doctest.testmod()


