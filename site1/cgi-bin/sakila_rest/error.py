__author__ = 'Ben'

import logging

def response(*messages):
    print("Status: 500 Internal Server Error" )
    print("Content-Type: plain/text; charset=UTF-8")
    print()
    logging.error("Error in sakila REST")

    for msg in messages:
        print(msg)
        logging.error(str(msg))

