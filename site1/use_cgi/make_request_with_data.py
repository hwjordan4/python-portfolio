__author__ = 'Ben'


import requests


query = {'x': 23, 'y': 'variable'}
r = requests.post("http://localhost:82/cgi-bin/printenv.py",data=query)
print(r.text)
