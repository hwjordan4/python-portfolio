__author__ = 'Ben'


#from json_with_dates import loads
import json_with_dates
import logging

# def request_to_sakila1(path=""):
#     from http.client import HTTPConnection, HTTPResponse
#     logging.debug('path'+path)
#     hconn = HTTPConnection('localhost', 82)
#     hconn.request('GET', '/cgi-bin/sakila_rest/sakila.py' + path)
#     resp = hconn.getresponse()
#     logging.debug('status'+str(resp.status))
#     bodyJ = resp.read()
#     logging.debug('body'+str(bodyJ))
#     bodystr = bodyJ.decode()
#     if resp.status == 200:
#         body = json_with_dates.loads(bodystr)
#         return ('K',body)
#     else:
#         return ('E', resp.status, bodystr)



def request_to_sakila(path="", body=None, method='GET', headers=None):
    from http.client import HTTPConnection, HTTPResponse
    import json_with_dates
    #print('path', path)
    if body:
        jbody = json_with_dates.dumps(body)
        enjbody = jbody.encode()
    else:
        enjbody = None
    hconn = HTTPConnection('localhost', 80)
    if headers:
        hconn.request(method, '/cgi-bin/sakila_rest/sakila.py' + path, body=enjbody,
            headers=headers)
    else:
        hconn.request(method, '/cgi-bin/sakila_rest/sakila.py' + path, body=enjbody)
    resp = hconn.getresponse()
    #print('status', resp.status)
    bodyJ = resp.read()
    #print('body',body)
    bodystr = bodyJ.decode()
    if resp.status == 200:
        #data = json_with_dates.loads(bodystr)
        #return data #json_with_dates.loads(hconn.getresponse().read().decode())
        body = json_with_dates.loads(bodystr)
        return ('K',body)
    else:
        return ('E', resp.status, bodystr)
        #print("response status", resp.status)
        #print('bodystr', bodystr)