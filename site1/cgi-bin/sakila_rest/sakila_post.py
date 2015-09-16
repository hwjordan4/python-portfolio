__author__ = 'Ben'

from json_with_dates import loads, dumps
import logging
from sakila_db import db_change
from sakila_get import send_data
import error

def create_customer(info):
    try:
        dataJ = info['data']
        data = loads(dataJ)
        resp = db_change.new_customer(data)
        if resp[0] == 'K':
            send_data(resp[1])
        else:
            error.response("error creating customer", *resp)
        send_data(id)
    except Exception as exc:
        error.page("error create_customer: ", exc)



def create_address(info):
    try:
        dataJ = info['data']
        data = loads(dataJ)
        resp = db_change.new_address(data)
        if resp[0] == 'K':
            send_data(resp[1])
        else:
            error.response("error creating address", *resp)
    except Exception as exc:
        error.page("Error creating address", exc)



def no_match():
    pass


dispatch_post = [
    (r'/customer$', create_customer),
    (r'/address$', create_address),
    (r'', no_match),
]