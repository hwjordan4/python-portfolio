#!c:/python34/python.exe

__author__ = 'Ben'

from request import request_to_sakila
import cgitb
cgitb.enable()
from jinja2 import Environment, FileSystemLoader
import error
import cgi

fs = cgi.FieldStorage()

values = {}

flist = fs.getlist('address')
if len(flist) != 1 or not flist[0]:
    error.page("address field not properly set")
    quit()
values['address'] = flist[0]

flist = fs.getlist('district')
if len(flist) != 1 or not flist[0]:
    error.page("district field not properly set")
    quit()
values['district'] = flist[0]

flist = fs.getlist('phone')
if len(flist) != 1 or not flist[0]:
    error.page("phone field not properly set")
    quit()
values['phone'] = flist[0]

flist = fs.getlist('city')
if len(flist) != 1 or not flist[0]:
    error.page("city field not properly set")
    quit()
values['city_id'] = flist[0]

flist = fs.getlist('postalcode')
if len(flist) > 1:
    error.page("Postal code field not properly set")
    quit()
elif len(flist) == 0 or not flist[0]:
    postalcode = None
else:
    values['postal_code'] = flist[0]


flist = fs.getlist('address2')
if len(flist) > 1:
    error.page("address2 field not properly set")
    quit()
elif len(flist) == 0 or not flist[0]:
    address2 = None
else:
    values['address2'] = flist[0]


resp = request_to_sakila("/address", body=values, method="Post",
                         headers={"Content-type": "application/json"})

if resp[0] != 'K':
    error.page("Error adding new address", values, *resp)
    quit()


context = {}




ldr = FileSystemLoader('templates')
env = Environment(loader=ldr)
template = env.get_template("address_create.html")
template_rendered = template.render(context)

print("Content-type: text/html")
print()
print(template_rendered)
