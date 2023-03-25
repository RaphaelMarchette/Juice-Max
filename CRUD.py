import json
import mysql.connector
from mysql.connector import Error

class Banco:
    def ConexaoBanco():
        con=None
        try:
            con = mysql.connector.connect(
                host = "localhost",
                user = "root",
                passwd = "L33TSUPAH4X0R",
                database = "juicemax",
                auth_plugin = "mysql_native_password"
            )
        except Error as ex:
            print(ex)
        return con

    def dql(query): #read
        vcon=Banco.ConexaoBanco()
        c=vcon.cursor(buffered=True)
        c.execute(query)
        res=c.fetchall()
        vcon.close()
        return res

    def dml(query): #create, update, delete
        try:
            vcon=Banco.ConexaoBanco()
            c=vcon.cursor(buffered=True)
            c.execute(query)
            vcon.commit()
            vcon.close()
        except Error as ex:
            print(ex)

class System:
    def __init__(self):
        BancoDados = 'Produto_Edit'
        extensao = '.json'
        extensao_db = '.db'
        self.titular = f'{BancoDados}{extensao}'
        self.db = f'{BancoDados}{extensao_db}'
        self.saw = self.saw()
        self.table_name     = self.table_name()
        self.table_lista    = self.table_lista()
        self.pre_columns    = self.pre_columns()
        self.pre_values     = self.pre_values()
        self.new_value      = self.new_value()
        self.code           = self.code()

    def saw(self):
         with open(self.titular, 'r', newline='', encoding='utf-8') as arquivo:
             saw = json.load(arquivo)
         return saw

    def table_name(self):
        x = self.saw.keys()
        for table_name in x:
            return table_name

    def table_lista(self):
        table_lista = self.saw[self.table_name]
        return table_lista

    def pre_columns(self):
        pre_columns = ()
        for k in self.table_lista[0].keys():
            pre_columns += k,
        return pre_columns

    def pre_values(self):
        pre_values = ()
        for v in self.table_lista[0].values():
            pre_values += v,
        return pre_values
    
    def new_value(self):
        self.__new_value = "laranja"
        return self.__new_value
    
    def code(self):
        self.__code = 500
        return self.__code

class Pre_Query:
    def Update_Table(self,saida,rows):
        saida.delete(*saida.get_children())
        for i in rows:
            saida.insert('', 'end', values=i)

    def Tirar_Parentes_e_Aspas(query):
        query = query.replace("'","")
        query = query.replace("(","")
        query = query.replace(")","")
        return query
    
    def fechar(self,formulario):
        formulario.destroy()

class CRUD(Pre_Query):

    def Creat_Dados_SQL(table_name, pre_values):
        query = f"INSERT INTO {table_name} VALUES {pre_values}"
        Banco.dml(query)

    def Read_Dados_SQL(table_name, pre_columns):
        query = f"SELECT {pre_columns} FROM {table_name}"
        query = Pre_Query.Tirar_Parentes_e_Aspas(query)
        Banco.dql(query)
        return query

    def Update_Dados_SQL(table_name, pre_columns, new_value,code):
        query = f'UPDATE {table_name} SET {pre_columns[1]} = "{new_value}" WHERE {pre_columns[0]} = {code}'
        query = Pre_Query.Tirar_Parentes_e_Aspas(query)
        Banco.dml(query)

    def Delete_Dados_SQL(table_name, pre_columns, code):
        query = f'DELETE FROM {table_name} WHERE {pre_columns[0]} = {code}'
        Banco.dml(query)

table_name  =   System().table_name
pre_columns =   System().pre_columns
pre_values  =   System().pre_values
new_value   =   System().new_value
code        =   System().code


#b = CRUD.Creat_Dados_SQL(table_name, pre_values)
b = CRUD.Read_Dados_SQL(table_name, pre_columns)
#b = CRUD.Update_Dados_SQL(table_name, pre_columns, new_value, code)
#b = CRUD.Delete_Dados_SQL(table_name, pre_columns, code)

#print(b)



