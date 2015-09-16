__author__ = 'Ben'

import db_access
import db_change

# address_columns = ['address_id', 'address', 'address2', 'district', 'city_id', 'postal_code',
#                    'phone', 'last_update']
# required_address_columns = [ 'address',  'district', 'city_id', 'phone']
# #

values = {
    'address': '123 Sesame Street', 'district': 'Montmarte', 'city_id': 50, 'phone': '123-555-1212'
}

code, value = db_change.new_address(values)

if code == 'K':
    print('success')
    print('new id ', value )
    addr = db_access.get_address_by_id(value)
    print('new address: ', addr)
else:
    print('error')
    print('error message ', value)

