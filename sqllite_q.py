# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:06:42 2015

@author: nilakant
"""

import sqlite3
conn = sqlite3.connect('sqlalchemy_example.db')
 
c = conn.cursor()
c.execute('SELECT * FROM person')
print (c.fetchall())
c.execute('SELECT * FROM address')
print (c.fetchall())
conn.close()