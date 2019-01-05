__author__ = 'user'

import cx_Oracle
con = cx_Oracle.connect("bank/bank@localhost/orcl")
cur = con.cursor()
