__author__ = 'Ben'

import super_path
import db_access
import db_change

custs = db_access.get_all_customers()
for c in custs:
    print(c)
db_change.delete_customer(600)

print("\n" + ('='*50) + "\n")

custs = db_access.get_all_customers()
for c in custs:
    print(c)