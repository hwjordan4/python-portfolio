#!c:/python34/python.exe
__author__ = 'Ben'


import cgi
import cgitb
cgitb.enable()

from request import request_to_sakila
from jinja2 import Environment, FileSystemLoader
import error

fldstor = cgi.FieldStorage()

customer_id_list = fldstor.getlist("customer_id")

if len(customer_id_list) != 1:
    error.page("There should be exactly one customer id sumbitted")
    exit()

customer_id = customer_id_list[0]

response = request_to_sakila("/customer/" + str(customer_id))

# error.page("returned from customer id search", response)

context = {}

if response[0] != 'K':
    error.page("Error getting customer data", response[1])
    exit()
cust_info = response[1]
context['cust_info'] = response[1]

address_id = cust_info['address_id']
response = request_to_sakila("/address/" + str(address_id))
if response[0] != 'K':
    #error.page("Error getting address data", response[1])
    #exit()
    address_info = None
else:
    address_info = response[1]
    context['address_info'] = address_info

city_info = None
if address_info:
    response = request_to_sakila("/city/" + str(address_info['city_id']))
    if response[0] == 'K':
        city_info = response[1]
        context['city_info'] = city_info

country_info = None
if city_info:
    response = request_to_sakila("/country/" + str(city_info['country_id']))
    if response[0] == 'K':
        country_info = response[1]
        context['country_info'] = country_info

response = request_to_sakila("/payment/customerid/" + str(customer_id))
if response[0] == 'K':
    payment_info = response[1]
    context['payment_info'] = payment_info
    response = request_to_sakila("/customer/total_payments/" + str(customer_id))
    payment_total = None
    if response[0] == 'K':
        payment_total = response[1]
        context['payment_total'] = payment_total
else:
    payment_info = None

response = request_to_sakila("/rental/customerid/" + str(customer_id))
if response[0] == 'K':
    rental_info = response[1]
    context['rental_info'] = rental_info
    # get a list of film titles
    #titles = []
    for rental in rental_info:
        response = request_to_sakila("/inventory/" + str(rental['inventory_id']))
        if response[0] == 'K':
            inventory = response[1]
            response = request_to_sakila("/film/" + str(inventory['film_id']))
            if response[0] == 'K':
                film_info = response[1]
                #titles.append(film_info['title'].title())
                rental['title'] = film_info['title'].title()
            else:
                #titles.append("xxx")
                rental['title'] = "xxx"
    #context['titles'] = titles
else:
    rental_info = None



print("Content-Type: text/html; charset=UTF-8")
print("")

ldr = FileSystemLoader('templates')
env = Environment(loader=ldr)

# the following is a custom filter that looks very much like
# an example in the Jinja2 documentation
def dateformat(value, format='%m/%d/%Y'):
    return value.strftime(format)
env.filters['dateformat'] = dateformat

template = env.get_template("customer_selected_display.html")
# template_rendered = template.render(cust_info=cust_info, address_info=address_info,
#                     city_info=city_info, country_info = country_info,
#                     payment_info=payment_info, payment_total=payment_total)
template_rendered =template.render(context)
print(template_rendered)


