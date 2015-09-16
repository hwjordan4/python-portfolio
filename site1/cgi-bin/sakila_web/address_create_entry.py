#!c:/python34/python.exe

__author__ = 'Ben'

from request import request_to_sakila
import cgitb
cgitb.enable()
from jinja2 import Environment, FileSystemLoader
import error

context = {}

cities = request_to_sakila('/city')
if cities[0] == 'K':
    context['cities'] = cities[1]
else:
    error.page('Cannot access city data', cities)
    quit()


ldr = FileSystemLoader('templates')
env = Environment(loader=ldr)
template = env.get_template("address_create_entry.html")
template_rendered = template.render(context)

print("Content-type: text/html")
print()
print(template_rendered)
