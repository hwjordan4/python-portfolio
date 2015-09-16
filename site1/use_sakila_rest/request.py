__author__ = 'Ben'


#from json_with_dates import loads
import json_with_dates
import logging

def request_to_sakila(path=""):
    from http.client import HTTPConnection, HTTPResponse
    logging.debug('path'+path)
    hconn = HTTPConnection('localhost', 82)
    hconn.request('GET', '/cgi-bin/sakila_rest/sakila.py' + path)
    resp = hconn.getresponse()
    logging.debug('status'+str(resp.status))
    bodyJ = resp.read()
    logging.debug('body'+str(bodyJ))
    bodystr = bodyJ.decode()
    if resp.status == 200:
        body = json_with_dates.loads(bodystr)
        return ('K',body)
    else:
        return ('E', resp.status, bodystr)



