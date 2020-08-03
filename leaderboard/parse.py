import requests
import json
import csv
import os.path

from datetime import datetime

def fetch():
  path = 'leaderboard.json'

  if not os.path.exists(path):
    print('Fetching new input...')
    input_url = 'https://adventofcode.com/2019/leaderboard/private/view/179752.json'
    session_cookie = open('../.aoc_session').read().strip()

    input_text = requests.get(input_url, cookies={'session': session_cookie}).text
    with open(path, 'w') as f:
      f.write(input_text)

  with open(path, 'r') as f:
    return json.load(f)


def parse_time(day, ts):
  start = datetime(2019, 12, int(day), 5)
  done = datetime.utcfromtimestamp(int(ts))
  d = done - start
  s = d.seconds
  days = d.days

  hours, remainder = divmod(s, 3600)
  minutes, seconds = divmod(remainder, 60)
  return '{:02}:{:02}:{:02}'.format(int(hours)+24*days, int(minutes), int(seconds))

def flatten_member(data):
  ret = dict(data)

  for day in data['completion_day_level']:
    for part in data['completion_day_level'][day]:
      k = "D%s-%s" % (day,part)
      ret[k] = parse_time(day, data['completion_day_level'][day][part]['get_star_ts'])

  return ret

data = fetch()

data = [flatten_member(x) for x in data['members'].values() if x['local_score'] > 0]


all_days = set()
for x in data:
  all_days |= (set([k for k in x.keys() if k.startswith('D')]))

with open('leaderboard.csv', 'w') as csvfile:
  headers = ['global_score', 'name', 'local_score']
  headers += sorted(all_days)

  writer = csv.DictWriter(csvfile, fieldnames=headers)
  writer.writeheader()
  for x in sorted(data, key=lambda r: -r['local_score']):
    writer.writerow( { k:x.get(k, '') for k in headers })

