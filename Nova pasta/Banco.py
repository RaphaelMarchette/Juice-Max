import mysql.connector
from mysql.connector import Error

def ConexaoBanco():
    con=None
    try:
        con=mysql.connector.connect(host='localhost', user='root', password='', database='base')
    except Error as ex:
        print(ex)
    return con

def dql(query): #read
    vcon=ConexaoBanco()
    print(vcon)
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query): #create, update, delete
    try:
        vcon=ConexaoBanco()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)