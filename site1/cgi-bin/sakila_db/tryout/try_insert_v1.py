__author__ = 'Ben'

import sqlite3
from datetime import datetime

conn = sqlite3.connect('sqlite-sakila.sq')
crs = conn.cursor()

customer_columns = ['active', 'address_id', 'create_date', 'customer_id', 'email', 'first_name', 'last_name',
                    'last_update', 'store_id']
customer_columns_initializable = ['active', 'address_id',  'email', 'first_name', 'last_name',
                                            'store_id']

crs.execute('select max(customer_id) from customer')
row = crs.fetchone()
if row:
    max_id = row[0]
else:
    max_id = 0

parmsD = {
    'active': 'Y', 'address_id': 0, 'create_date': datetime.now(), 'customer_id': max_id+1,
    'email': '', 'first_name': '', 'last_name': '',
    'last_update': datetime.now(), 'store_id': 0
}

values = {
    'first_name': 'John', 'last_name': 'Doe'
}

for (k,v) in values.items():
    if k in customer_columns_initializable:
        parmsD[k] = v
parms = []
for k in customer_columns:
    parms.append(parmsD[k])

cmd = '''
  insert into customer
  (active, address_id, create_date, customer_id, email, first_name, last_name, last_update, store_id)
  values(?,?,?,?, ?, ?, ?, ? ,?)

'''
print(parms)
crs.execute(cmd, parms)
print(crs.fetchall())
conn.commit()


conn.close()