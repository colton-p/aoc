import os
import re
import itertools

import requests

import util.input_stats

class Input:
  @classmethod
  def for_date(cls, day, year=2019, test=False, strip = True):
    return cls(_input_rows(day, year, test, strip))

  def __init__(self, rows):
    self.rows = rows

  ####

  def line_delimited(self):
    grouped = itertools.groupby(self.rows, lambda x: x != '')
    return [tuple(v) for (k,v) in grouped if k]

  def single_string(self):
    """
    Single unparsed row of input.
    >>> Input(['hello']).single_string()
    'hello'
    """
    (row,) = self.rows
    return row

  def single_int(self):
    """
    Single integer.
    >>> Input(['1234']).single_int()
    1234
    """
    (row,) = self.int_list()
    return row

  def numeric_tuples(self):
    """
    Extract integers from each row.
    >>> Input(['123 x 456', '11 -22']).numeric_tuples()
    [(123, 456), (11, -22)]
    """
    return [tuple(ints(row)) for row in self.rows]

  def tuples(self, split= ' '):
    """
    Split each row, cast integers.
    >>> Input(['hello 123', 'catch -22']).tuples()
    [('hello', 123), ('catch', -22)]
    """
    return [
      tuple(safe_int(x) for x in row.split(split))
      for row in self.rows
    ]
  
  def word_tuples(self):
    """
    Split each row on non-word characters, cast ints
    >>> Input(['hello: 123', 'catch = -22']).tuples2()
    [('hello', 123), ('catch', 22)]
    """
    return [
      tuple(safe_int(x) for x in re.split('\W+', row))
      for row in self.rows
    ]

  def int_list(self):
    """
    Cast each row to integer.
    >>> Input(['123', 'hi', '-22 456']).int_list()
    [123, 'hi', '-22 456']
    """
    return [safe_int(x) for x in self.rows]

  def ints(self):
    """
    Extract all integers from single row.
    >>> Input(['hi 123-45xxx789']).ints()
    [123, -45, 789]
    """
    (row,) = self.rows
    return ints(row)

  def pints(self):
    """
    Extract all positive integers from single row.
    >>> Input(['123-45xxx789']).pints()
    [123, 45, 789]
    """
    (row,) = self.rows
    return pints(row)
  
  def safe_inputs(self):
    def safe(func):
      try:
        return func.__call__()
      except:
        return
    
    return (
      safe(self.single_string),
      safe(self.single_int),
      safe(self.int_list),
      safe(self.numeric_tuples),
      safe(self.tuples),
      safe(self.word_tuples),
    )

  ####


  def pp_analyze(self):
    stats = util.input_stats.InputStats(self.rows)

    (kind, details)  = stats.guess_kind()

    n_rows = stats.n_rows()
    (min_row, max_row) = stats.n_cols()

    print('.' * 16)
    print("  Kind: %s (%s)" % (kind, details))
    print("n rows: %4d" % n_rows)
    if min_row == max_row:
      print("n cols: %4d" % (max_row))
    else:
      print("n cols: %4d-%4d" % (min_row, max_row))
    print('.' * 16)
    print('')

  def peak(self, nrows=10, ncols=80):
    print('---- begin input ----')
    for row in self.rows[:nrows]:
      s = str(row)
      if len(s) > ncols:
        print(s[:ncols], 'and more...')
      else:
        print(s)
    if len(self.rows) > nrows:
      print('...')
    print('----  end input  ----')
    print('')


def _input_rows(day, year=2019, test=False, strip=True):
  path = 'inputs/%s-%s.txt' % (year, day)
  if test: path += '.test'

  print(path, 'exists?', os.path.exists(path))
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

def ints(line):
  """
  >>> ints('1 -2 3')
  [1, -2, 3]

  >>> ints('abc-12 - 34')
  [-12, 34]

  >>> ints('abcdef')
  []
  """
  return [int(x) for x in re.findall(r'-?\d+', line)]


def pints(line):
  return [int(x) for x in re.findall('\d+', line)]

if __name__ == '__main__':
  import doctest
  globs = {
    'single': Input(['hello 123']),
    'double': 'hello 123\nbye 456'
  }
  doctest.testmod(extraglobs=globs)



