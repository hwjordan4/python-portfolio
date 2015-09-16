__author__ = 'Ben'


import request


r = request.get("http://localhost:82/cgi-bin/printenv.py")
print(r.text)
