__author__ = 'Ben'

import db_access
import db_change



values = {
    'first_name': 'John', 'last_name': 'Doe', 'email': 'abc@k.e',
}
id = db_change.new_customer(values)

# custs = get_all_customers()
# for c in custs:
#     print(c)

cust = db_access.get_customer_by_id(id)
print(cust)


db_change.update_customer(id, {'email': 'abc@students.kennesaw.edu', 'last_name': 'Mason'})


cust = db_access.get_customer_by_id(id)
print(cust)


db_change.delete_customer(id)

cust = db_access.get_customer_by_id(id)
print(cust)
