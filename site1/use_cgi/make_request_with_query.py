__author__ = 'Ben'


import request


query = {'x': 23, 'y': 'variable'}
r = request.get("http://localhost:82/cgi-bin/printenv.py", params=query)
print(r.text)
