#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='grantdata',
                                       user='root',
                                       password='Terricola07.')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()

