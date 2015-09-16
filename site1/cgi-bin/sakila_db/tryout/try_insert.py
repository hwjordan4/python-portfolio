__author__ = 'Ben'

import db_access
import db_change



values = {
    'first_name': 'John', 'last_name': 'Doe', 'email': 'abc@k.e',
    'store_id': 20, 'address_id': 30,
}
resp = db_change.new_customer(values)

if resp[0] == 'K':
    id = resp[1]
    print("response", resp)
    cust = db_access.get_customer_by_id(id)
    print(cust)


    db_change.update_customer(id, {'email': 'abc@students.kennesaw.edu', 'last_name': 'Mason'})


    cust = db_access.get_customer_by_id(id)
    print(cust)


    db_change.delete_customer(id)

    cust = db_access.get_customer_by_id(id)
    print(cust)
else:
    print("return error", resp)
    print()