import json
import mysql.connector
from mysql.connector import Error


class Banco:
    def __init__(self):
        self.__ConexaoBanco = self.ConexaoBanco()

    def ConexaoBanco(self):
        con=None
        try:
            con=mysql.connector.connect(host='localhost', user='root', password='L33TSUPAH4X0R', database='JuiceMax')
        except Error as ex:
            print(ex)
        return con

    def dql(self, query): #read
        vcon=self.__ConexaoBanco
        print(vcon)
        c=vcon.cursor()
        c.execute(query)
        res=c.fetchall()
        vcon.close()
        return res

    def dml(self, query): #create, update, delete
        try:
            vcon=self.__ConexaoBanco
            c=vcon.cursor()
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

class Pre_Query:
    def Update_Table(self,saida,rows):
        saida.delete(*saida.get_children())
        for i in rows:
            saida.insert('', 'end', values=i)

    def Tirar_Parentes_e_Aspas(self,query):
        query = query.replace("'","")
        query = query.replace("(","")
        query = query.replace(")","")
        return query
    
    def fechar(self,formulario):
        formulario.destroy()

class CRUD(System, Pre_Query, Banco):
    def Creat_Dados_SQL(self,saida,formulario,campos):
        valores = ()
        for i in range(len(campos)):
            g = campos[i].get()
            valores += f"{g}",
        query = f"INSERT INTO {System().table_name} {System().pre_columns} VALUES {valores}"
        self.dml(query)
        self.Read_Dados_SQL(saida)
        self.fechar(formulario)

    def Read_Dados_SQL(self,saida):
        query = f"SELECT {System().pre_columns} from {System().table_name}"
        query = self.Tirar_Parentes_e_Aspas(query)
        self.Update_Table(saida,self.dql(query))

    def Update_Dados_SQL(self,saida,formulario,campos):
        kv = ()
        for i in range(2,len(campos)):
            kv += f'{System().pre_columns[i]} = {campos[i].get()}',
        query = f'UPDATE {System().table_name} SET {kv} WHERE {System().pre_columns[0]} = "{campos[0].get()}"'
        query = self.Tirar_Parentes_e_Aspas(query)
        self.dml(query)
        self.Read_Dados_SQL(saida)
        self.fechar(formulario)

    def Delete_Dados_SQL(self,saida,formulario,campos):
        excluir = f"DELETE FROM {System().table_name} WHERE {System().pre_columns[0]} ='{campos[0].get()}'"
        self.dml(excluir)
        self.Read_Dados_SQL(saida)
        self.fechar(formulario)





b = System()

print(b.saw)
print()
print(b.table_name)
print()
print(b.table_lista)
print()
print(b.pre_columns)
print()
print(b.pre_values)
