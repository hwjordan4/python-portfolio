__author__ = 'Ben'

from json_with_dates import loads, dumps

def request_to_sakila(path="", body=None, method='GET'):
    from http.client import HTTPConnection, HTTPResponse
    import json_with_dates
    #print('path', path)
    hconn = HTTPConnection('localhost', 82)
    hconn.request(method, 'http://localhost/cgi-bin/sakila_rest/sakila.py' + path, body=body,
        headers={'content-type': 'applicaton/json'})
    resp = hconn.getresponse()
    #print('status', resp.status)
    bodyJ = resp.read()
    #print('body',body)
    bodystr = bodyJ.decode()
    if resp.status == 200:
        #data = json_with_dates.loads(bodystr)
        #return data #json_with_dates.loads(hconn.getresponse().read().decode())
        body = loads(bodystr)
        return body
    else:
        print("response status", resp.status)
        print('bodystr', bodystr)


values = {
    'first_name': 'John', 'last_name': 'Doe', 'email': 'abc@k.e',
}
jval = dumps(values)
request_to_sakila(path="/customer", body=jval, method='POST')

