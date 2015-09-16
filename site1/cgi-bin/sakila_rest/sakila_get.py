__author__ = 'Ben'

import super_path
#from json_with_dates import dumps
import json_with_dates
import json
from sakila_db import db_access
import logging


def send_data(data):
    logging.debug(str(data))
    dataJ = json.dumps(data)
    logging.debug("custJ " + str(dataJ))
    lng = len(dataJ)
    logging.debug("len " + str(lng))
    print("Content-Type: application/json; charset=UTF-8")
    print("Content-Length: " + str(lng))
    print()
    print(dataJ)


def all_customers(info):
    customers = db_access.get_all_customers()
    send_data(customers)
    # custJ = dumps(customers)
    # #logging.info("custJ " + str(custJ))
    # lng = len(custJ)
    # #logging.info("len " + str(lng))
    # print("Content-Type: application/json; charset=UTF-8")
    # print("Content-Length: " + str(lng))
    # print()
    # print(custJ)


def all_cities(info):
    data = db_access.get_all_cities()
    send_data(data)

def all_stores(info):
    data = db_access.get_all_stores()
    send_data(data)


def customer_by_id(info):
    id = info['match'].group(1)
    cust = db_access.get_customer_by_id(id)
    send_data(cust)


def country_by_id(info):
    id = info['match'].group(1)
    cntry = db_access.get_country_by_id(id)
    send_data(cntry)


def city_by_id(info):
    id = info['match'].group(1)
    city = db_access.get_city_by_id(id)
    send_data(city)


def address_by_id(info):
    id = info['match'].group(1)
    addr = db_access.get_address_by_id(id)
    send_data(addr)


def inventory_by_id(info):
    id = info['match'].group(1)
    data = db_access.get_inventory_by_id(id)
    send_data(data)


def film_by_id(info):
    id = info['match'].group(1)
    data = db_access.get_film_by_id(id)
    send_data(data)


def store_by_id(info):
    id = info['match'].group(1)
    data = db_access.get_store_by_id(id)
    send_data(data)


def rentals_by_customer(info):
    id = info['match'].group(1)
    data = db_access.get_rentals_by_customer(id)
    send_data(data)


def payments_by_customer(info):
    id = info['match'].group(1)
    data = db_access.get_payments_by_customer(id)
    send_data(data)

def total_payments_by_customer(info):
    id = info['match'].group(1)
    data = db_access.total_payments_by_customer(id)
    send_data(data)

def no_match(info):
    message = "Path " + info["path"] + " not found"
    print("Status: 404 Not Found" )
    print("Content-Type: plain/text; charset=UTF-8")
    print("Content-Length: " + str(len(message)))
    print()
    print(message)


dispatch_get = [
    (r'/customer$', all_customers),
    (r'/city$', all_cities),
    (r'/store$', all_stores),
    (r'/country/(\d+)$', country_by_id),
    (r'/customer/(\d+)$', customer_by_id),
    (r'/city/(\d+)$', city_by_id),
    (r'/address/(\d+)$', address_by_id),
    (r'/inventory/(\d+)$', inventory_by_id),
    (r'/film/(\d+)$', film_by_id),
    (r'/store/(\d+)$', store_by_id),
    (r'/rental/customerid/(\d+)$', rentals_by_customer),
    (r'/payment/customerid/(\d+)$', payments_by_customer),
    (r'/customer/total_payments/(\d+)$', total_payments_by_customer),
    (r'', no_match),
]

# dispatch_get = {
#     r'/customer$': all_customers,
#     r'/city$': all_cities,
#     r'/customer/(\d+)$': customer_by_id,
#     r'/city/(\d+)$': city_by_id,
#     r'/address/(\d+)$': address_by_id,
#     r'/inventory/(\d+)$': inventory_by_id,
#     r'/film/(\d+)$': film_by_id,
#     r'/rental/customerid/(\d+)$': rentals_by_customer,
#     r'/payment/customerid/(\d+)$': payments_by_customer,
#     r'': no_match,
# }
