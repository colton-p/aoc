from bs4 import BeautifulSoup
import time
import requests


import urllib.parse
import os.path
def fetch(url):
  parsed = urllib.parse.urlparse(url)
  path = 'data/' + parsed.path.replace('/', '_')

  if not os.path.exists(path):
    result = requests.get(url)
    with open(path, 'w') as f:
      f.write(result.text)

  with open(path, 'r') as f:
    return f.readlines()




page = ''.join(open('Main Page - Competitive Programming Algorithms.htm', 'r').readlines())


print(page)
soup = BeautifulSoup(page, 'html.parser')

links = [x.attrs['href'] for x in soup.find_all('a') if x.attrs['href'].startswith("https://cp-algorithms.com/") ]
for x in links:
  print(x)
  fetch(x)


