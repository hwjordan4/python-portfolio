#!c:/python34/python.exe

__author__ = 'Ben'

from sakila_get import dispatch_get
from sakila_post import dispatch_post
from os import environ
import sys
import re
import logging


logging.basicConfig(filename='server.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def dispatch(path, data, dispatch_table):
    logging.info("dispatch started")
    for (rgx, handler) in dispatch_table:
        match = re.match(rgx, path)
        logging.info("rgx {}   path {}   match {}".format(rgx, path, match))
        if match:
            handler({'match': match, 'data': data, 'path': path})
            return
    logging.error("dispatch table exhausted")
    print("Status: 500 Internal Server Error" )
    print("Content-Type: plain/text; charset=UTF-8")
    print()
    print("no more dispatch table")

#print("Content-Type: application/json; charset=UTF-8")
#print()

pi = environ.get("PATH_INFO", "")
method = environ.get('REQUEST_METHOD', "").lower()
data = sys.stdin.read()


if method == 'get':
    logging.info('get')
    logging.info(str(dispatch_get))
    dispatch(pi, data, dispatch_get)
    logging.debug("Dispatch finished")
elif method == 'post':
    dispatch(pi, data, dispatch_post)
# elif method == 'put':
#
#     pass
else:
    print("Status: 405 Method Not Allowed" )
    print("Content-Type: plain/text; charset=UTF-8")
    print()
    print("incorrect http method")


