#!c:/python34/python.exe

from request import request_to_sakila
import cgitb
cgitb.enable()
from jinja2 import Environment, FileSystemLoader


__author__ = 'Ben'


path = "/customer"
resp = request_to_sakila(path)

print("Content-type: text/html")
print()

if resp[0] == 'K':
    cust_list = sorted(resp[1], key=lambda x : x['last_name'] + x['first_name'])
    ldr = FileSystemLoader('templates')
    env = Environment(loader=ldr)
    template = env.get_template("customer_select.html")
    template_rendered = template.render(customers = cust_list)
    print(template_rendered)
else:
    print("error")

