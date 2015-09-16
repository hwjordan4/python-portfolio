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
    ldr = FileSystemLoader('templates')
    env = Environment(loader=ldr)
    template = env.get_template("customer_list.html")
    template_rendered = template.render(customers = resp[1])
    print(template_rendered)
else:
    print("error")

