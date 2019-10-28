import csv
import json
import os.path
import requests
import itertools
from datetime import datetime

def get_leaderboard():
  path = 'scores.json'

  if not os.path.exists(path):
    print 'Fetching ...'
    url = 'https://adventofcode.com/2018/leaderboard/private/view/179752.json'
    input = requests.get(url, cookies={'session': open('.aoc_session').read().strip()}).text
    with open(path, 'w') as f:
      f.write(input)

  with open(path, 'r') as f:
    return json.load(f)


def all_days(leaderboard):
  all_days = set()
  for member in leaderboard.values():
    member_days = set(member.get('completion_day_level', {}).keys())
    all_days |= member_days
  return sorted((all_days))


def member_to_row(member, all_days):
  solves = member['completion_day_level']

  times = []
  for day in all_days:
    day_results = solves.get(day, {})
    for part in ['1', '2']:
      ts = day_results.get(part, {}).get('get_star_ts', None)
      if ts is not None:
        times += [datetime.fromtimestamp(float(ts)) - datetime(2018, 12, int(day))]
      else:
        times += [None]

  return tuple([member['name'], member['global_score'], member['local_score'], member['stars']] + times)


leaderboard = get_leaderboard()['members']

members = leaderboard.keys()

days = [d for d in all_days(leaderboard)]
parts = []
for d in days:
  parts += ['%s-1' % d, '%s-2' % d]

with open('scores.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)

  writer.writerow(['name', 'global', 'local', 'stars'] + parts)
  for member in leaderboard.values():
    writer.writerow(member_to_row(member, all_days(leaderboard)))

