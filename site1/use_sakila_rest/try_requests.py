__author__ = 'Ben'

from json_with_dates import loads

def request_to_sakila(path=""):
    from http.client import HTTPConnection, HTTPResponse
    import json_with_dates
    #print('path', path)
    hconn = HTTPConnection('localhost', 82)
    #hconn.request('GET', 'http://localhost/cgi-bin/sakila_rest/sakila.py' + path)
    hconn.request('GET', '/cgi-bin/sakila_rest/sakila.py' + path)
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


#customers = request_to_sakila("/customer/5")
cid = 400
cst = request_to_sakila("/customer/" + str(cid))
print(cst)
addr = request_to_sakila("/address/" + str(cst['address_id']))
print(addr)
# # cities = get_all_cities()
# # for c in cities:
# #     print(c)
# print(get_country_by_id(40))
cit = None
if addr:
    cit = request_to_sakila("/city/" + str(addr['city_id']))
    print(cit)
if cit:
    cntry = request_to_sakila("/country/" + str(cit['country_id']))
    print(cntry)
rntls = request_to_sakila("/rental/customerid/" + str(cid))
for rn in rntls:
    print(rn)
    invnt = request_to_sakila("/inventory/" + str(rn['inventory_id']))
    film = request_to_sakila("/film/" + str(invnt['film_id']))
    print(film['title'])
pmnts = request_to_sakila("/payment/customerid/" + str(cid))
for p in pmnts:
    print(p)
tot_payment = request_to_sakila("/customer/total_payments/" + str(cid))
print('total payments:', '{:.2f}'.format(tot_payment))
# print(sorted(cst.keys()))