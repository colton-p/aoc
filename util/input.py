import os
import re

import requests

class Input:
  @classmethod
  def for_date(cls, day, year=2019, test=False, strip = True):
    return cls(input_rows(day, year, test, strip))

  def __init__(self, rows):
    self.rows = rows


  def peak(self, nrows=10, ncols=80):
    print('---- begin input ----')
    for row in self.rows[:nrows]:
      print(str(row)[:ncols])
    print('----  end input  ----')
    print('')

  def single_string(self):
    (row,) = self.rows
    return row

  def numeric_tuples(self):
    return [extract_numbers(row) for row in self.rows]

  def tuples(self, split= ' '):
    return [
      tuple(safe_int(x) for x in row.split(split))
      for row in self.rows
    ]

  def int_list(self):
    return [safe_int(x) for x in self.rows]


  def pp_analyze(self):
    (kind, n_rows, max_row, min_row, _x) = self.__analyze()
    print('.' * 16)
    print("  Kind: %s" % kind)
    print("n rows: %4d" % n_rows)
    if min_row == max_row:
      print("n cols: %4d" % (max_row))
    else:
      print("n cols: %4d-%4d" % (min_row, max_row))
    print('.' * 16)
    print('')

  def __analyze(self):
    n_rows = len(self.rows)
    row_lens = list(map(len, self.rows))
    kind = "???"

    if n_rows == 1:
      if safe_int(self.rows[0]) == self.rows[0]:
        if re.match('^[A-Za-z]+$', self.rows[0]):
          kind = "one string"
        else:
          kind = "one line"
      else:
        kind = "one number"
    else:
      if all( [type(safe_int(x)) == int for x in self.rows]):
        kind = 'list of numbers'

      if len(set(row_lens))==1:
        kind = "grid (even row lengths)"

    return (kind, n_rows, max(row_lens), min(row_lens), len(set(row_lens))==1)


def input_rows(day, year=2019, test=False, strip=True):
  path = 'inputs/%s-%s.txt' % (year, day)
  if test: path += '.test'

  print(path, os.path.exists(path))
  if not os.path.exists(path):
    print('Fetching new input...')
    input_url = 'https://adventofcode.com/%s/day/%s/input' % (year, day)
    session_cookie = open('.aoc_session').read().strip()
    print(input_url)

    input_text = requests.get(input_url, cookies={'session': session_cookie}).text
    with open(path, 'w') as f:
      f.write(input_text)

  with open(path, 'r') as f:
    if strip:
      return [line.strip() for line in f]
    else:
      return [line for line in f]

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

