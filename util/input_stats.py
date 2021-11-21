import collections
import re

class InputStats:
    def __init__(self, rows):
        self.rows = rows

    def n_rows(self):
        return len(self.rows)
    
    def n_cols(self):
        row_lens = [len(r) for  r in self.rows]

        return min(row_lens), max(row_lens)

    def characters(self):
        c = collections.Counter()

        for row in self.rows:
            c.update(row)
        
        return c
    
    def guess_kind(self):
        if self.n_rows() == 1:
            row = self.rows[0]
            if is_int(row): 
                return ('one number', len(row))
            if re.match('^\w+$', row):
                return 'one string', len(row)

            if all(is_int(val) for val in re.split('\W+', row)):
                return ('single list of numbers', ',')

        
        if all(is_int(row) for row in self.rows):
            return 'list of single numbers', len(self.rows)


        (v, sep) = is_numeric_tuple(self.rows[0])
        if v:
            return ('numeric tuple', f'(n={v} sep={sep})')

        if self.n_rows() == 1:
            return 'one line', len(row)

        if len(set(self.n_cols())) == 1:
            return 'grid (even row lengths)', (self.n_cols()[0], len(self.rows))
        
        return (None, self.characters().most_common(n=3))

        

def is_numeric_tuple(row):
    m = re.match(r'^(\d+)(\D*)', row)

    if not m: return (None, None)
    sep = m.group(2)

    split = row.split(sep)
    if all(is_int(v) for v in split):
        return (len(split), sep)
    return (False, False)

    m = re.match(rf'^((\d+){sep})+\d+$', row)
    print(m.group)

    return (True, sep,)



def is_int(value):
  try:
    int(value)
    return True
  except ValueError:
    return False