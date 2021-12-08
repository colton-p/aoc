import argparse
import os
import sys



def create_boilerplate(args):
  day = args.day
  year = args.year
  filename = '%d-%.2d.py' % (year, day)
  
  out = ''.join([l for l in open('template.py', 'r')])
  out = out.replace('<year>', str(year))
  out = out.replace('<day>', str(day))

  with open(filename, args.filemode) as f:
    f.write(out)
  
  return filename

def create_test_input(args):
  filename = f"inputs/{args.year}-{args.day}.txt.test"
  with open(filename, args.filemode) as f:
    return filename

def create_go_script(script_file):
  out = f"python3 {script_file}"
  with open('go', 'w') as f:
    f.write(out)

parser = argparse.ArgumentParser()
parser.add_argument('day', type=int, choices=range(1, 26))
parser.add_argument('year', nargs='?', type=int, choices=range(2015, 2022))

parser.add_argument('--overwrite', default='x', action='store_const', const='w',dest='filemode')

args = parser.parse_args()

print(f"day {args.day} ({args.year})")
script_file = create_boilerplate(args)
print(f"... {script_file} created")
test_input = create_test_input(args)
print(f"... {test_input} created")

create_go_script(script_file)
print(f"... go script created: {open('go', 'r').readlines()}")

