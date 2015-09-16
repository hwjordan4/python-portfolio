__author__ = 'Ben'

import sqlite3
from datetime import datetime
from .db import exec_cmd, exec_for_one



def get_all_customers():
    '''
        This function returns a list of dictionaries containing data from the customers table in Classic Models.
        All columns of data are returned.
        Each dictionary represents one customer
        The keys in each dictionary are the column names and the associated values are the values in that column for that row
    '''
    return exec_cmd('select * from customer')


def get_all_cities():
    cmd = 'select * from city, country where city.country_id = country.country_id order by city.city'
    return exec_cmd(cmd)


def get_all_stores():
    return exec_cmd('select * from store')



def get_customer_by_id(id):
    return exec_for_one('select * from customer where customer_id = ?', [id])


#
#   Get by id
#


def get_country_by_id(id):
    return exec_for_one('select * from country where country_id = ?', [id])


def get_city_by_id(id):
    cityresp = exec_for_one('select * from city where city_id = ?', [id])
    if cityresp:
        cntryresp = get_country_by_id(cityresp['country_id'])
        if cntryresp:
            cityresp['country_name'] = cntryresp['country']
        else:
            cityresp['country_name'] = "not found"
    else:
        cityresp['country_name'] = "not found"
    return cityresp


def get_address_by_id(id):
    return exec_for_one('select * from address where address_id = ?', [id])


def get_inventory_by_id(id):
    return exec_for_one('select * from inventory where inventory_id = ?', [id])


def get_film_by_id(id):
    return exec_for_one('select * from film where film_id = ?', [id])


def get_store_by_id(id):
    return exec_for_one('select * from store where store_id = ?', [id])

#
#  Lists by id
#

def get_rentals_by_customer(customer_id):
    return exec_cmd('select * from rental where customer_id = ?', [customer_id])


def get_payments_by_customer(customer_id):
    return exec_cmd('select * from payment where customer_id = ?', [customer_id])


#
# Utilities
#

def total_payments_by_customer(customer_id):
    pmts = get_payments_by_customer(customer_id)
    total = 0
    for p in pmts:
        total += p['amount']
    return total



if __name__ == "__main__":
    # custs = get_all_customers()
    # for c in custs:
    #     print(c)
    cid = 600
    cst = get_customer_by_id(cid)
    print(cst)
    addr = get_address_by_id(cst['address_id'])
    print(addr)
    # cities = get_all_cities()
    # for c in cities:
    #     print(c)
    #print(get_country_by_id(40))
    cit = get_city_by_id(addr['city_id'])
    print(cit)
    cntry = get_country_by_id(cit['country_id'])
    print(cntry)
    rntls = get_rentals_by_customer(cid)
    for rn in rntls:
        print(rn)
        invnt = get_inventory_by_id(rn['inventory_id'])
        film = get_film_by_id(invnt['film_id'])
        print(film['title'])
    pmnts = get_payments_by_customer(cid)
    for p in pmnts:
        print(p)
    print('total payments:', '{:.2f}'.format(total_payments_by_customer(cid)))
    print(sorted(cst.keys()))