__author__ = 'Ben'

import sqlite3


def dictionary_factory(cursor, row):
    """
    Create a dictionary from rows in a cursor result.
    The keys will be the column names.
    :param cursor: A cursor from which a query row has just been fetched
    :param row: The query row that was fetched
    :return: A dictionary associating column names to values
    """
    col_names = [d[0] for d in cursor.description]
    return dict(zip(col_names, row))

from os.path import split, join


def get_connection():
    this_dir = split(__file__)[0]
    fname = join(this_dir, 'sqlite-sakila.sq')
    conn = sqlite3.connect(fname)
    conn.row_factory = dictionary_factory
    return conn



def exec_cmd(cmd, args=[]):
    sakila = get_connection()
    try:
        crs = sakila.cursor()
        crs.execute(cmd, args)
        return crs.fetchall()
    finally:
        sakila.close()

def exec_for_one(cmd, args=[]):
    tmp = exec_cmd(cmd, args)
    if len(tmp) > 0:
        return tmp[0]
    else:
        return None
