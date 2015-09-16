__author__ = 'Ben'

import sqlite3
from datetime import datetime
import logging
from . db import get_connection


customer_columns = ['active', 'address_id', 'create_date', 'customer_id', 'email', 'first_name', 'last_name',
                    'last_update', 'store_id']
customer_columns_initializable = ['active', 'address_id',  'email', 'first_name', 'last_name',
                                            'store_id']
required_customer_columns = ['store_id', 'first_name', 'last_name', 'email', 'address_id',]
    # 'active' defaults to 1
not_allowed_customer_columns=['customer_id', 'last_update', 'create_date']

def new_customer(customer_info):
    """
     Create a new customer in the database given the data for that address.
     :param customer_info: A dictionary using column names as keys.
     :return: ('K',id of newly created address), if created.
             ('E', error) if not
    """
    try:
        # check that required columns are provided
        for rcc in required_customer_columns:
            if rcc not in customer_info.keys():
                return ('E', 'column ' + rcc + ' value is required')

        # check that disallowed columns are not provided
        for nacc in not_allowed_customer_columns:
            if nacc in customer_info.keys():
                return ('E', 'column ' + nacc + ' not allowed in request')

        # check that columns are valid
        for k in customer_info.keys():
            if k not in customer_columns:
                return ('E', 'column ' + k  + ' is invalid')

        # build list of column names and values
        namesl = []
        values = []
        for (k,v) in customer_info.items():
            namesl.append(k)
            values.append(v)
        namesl.append('last_update')
        values.append(datetime.now())
        namesl.append('create_date')
        values.append(datetime.now())

        # get new id
        conn = get_connection()
        crs = conn.cursor()
        crs.execute("pragma FOREIGN_KEYS=ON")
        crs.execute('select max(customer_id) from customer')
        row = crs.fetchone()
        if row:
            max_id = row[0]
        else:
            max_id = 0
        new_id = max_id+1
        namesl.append('customer_id')
        values.append(new_id)

        # create SQL command and execute
        cmd_template = 'insert into customer ({}) values ({})'
        names = ",".join(namesl)
        valpoints = "?," * (len(namesl)-1) + "?"
        cmd = cmd_template.format(names, valpoints)
        logging.info("insert address command is " + cmd)
        crs.execute(cmd, values)
        conn.commit()
        conn.close()
        return 'K', new_id
    except Exception as exc:
        #raise exc
        return "E", str(exc)


address_columns = ['address_id', 'address', 'address2', 'district', 'city_id', 'postal_code',
                   'phone', 'last_update']
required_address_columns = [ 'address',  'district', 'city_id', 'phone']
# code for new address provides address_id, last_update
not_allowed_address_columns = ['address_id', 'last_update']

def new_address(address_info):
    """
    Create a new address in the database given the data for that address.
    :param address_info: A dictionary using column names as keys.
    :return: ('K',id of newly created address), if created.
            ('E', error) if not
    """
    try:
        # check that required columns are provided
        for rac in required_address_columns:
            if rac not in address_info.keys():
                return ('E', 'column ' + rac + ' value is required')

        # check that disallowed columns are not provided
        for naac in not_allowed_address_columns:
            if naac in address_info.keys():
                return ('E', 'column ' + naac + ' not allowed in request')

        # check that columns are valid
        for k in address_info.keys():
            if k not in address_columns:
                return ('E', 'column ' + k  + ' is invalid')

        # build list of column names and values
        namesl = []
        values = []
        for (k,v) in address_info.items():
            namesl.append(k)
            values.append(v)
        namesl.append('last_update')
        values.append(datetime.now())

        # get new id
        conn = get_connection()
        crs = conn.cursor()
        crs.execute('select max(address_id) from address')
        row = crs.fetchone()
        if row:
            max_id = row[0]
        else:
            max_id = 0
        new_id = max_id+1
        namesl.append('address_id')
        values.append(new_id)

        # create SQL command and execute
        cmd_template = 'insert into address ({}) values ({})'
        names = ",".join(namesl)
        valpoints = "?," * (len(namesl)-1) + "?"
        cmd = cmd_template.format(names, valpoints)
        logging.info("insert address command is " + cmd)
        crs.execute(cmd, values)
        conn.commit()
        conn.close()
        return 'K', new_id
    except Exception as exc:
        #raise exc
        return "E", str(exc)


def update_customer(customer_id, customer_information):
    conn = get_connection()
    crs = conn.cursor()
    crs.execute('select max(customer_id) from customer')
    row = crs.fetchone()
    if row:
        max_id = row[0]
    else:
        max_id = 0
    new_id = max_id+1
    parmsD = {
        'last_update': datetime.now()
    }
    for (k,v) in customer_information.items():
        if k in customer_columns_initializable:
            parmsD[k] = v
    values = []
    cmd = 'update customer set '
    sets = []
    for (k,v) in parmsD.items():
        values.append(parmsD[k])
        sets.append(' ' + k + ' = ? ')
    values.append(customer_id)
    cmd = 'update customer set '
    cmd += ', '.join(sets)
    cmd += 'where customer_id = ?'
    crs.execute(cmd, values)
    conn.commit()
    conn.close()


def delete_customer(customer_id):
    conn = get_connection()
    crs = conn.cursor()
    cmd = 'delete from customer where customer_id=? '
    crs.execute(cmd, [customer_id])
    conn.commit()
    conn.close()





if __name__ == "__main__":
    pass