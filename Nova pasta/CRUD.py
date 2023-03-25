from Banco import dql, dml


table = "vendas"
field = "nome_produto"
field_value = "Macarrão"
value = 4


update_where = field
update_new_value = 2
where_value = field_value

class CRUD:
    def create(table, field, value):
        query = f'INSERT INTO {table} (nome_produto, valor) VALUES ("{field_value}", "{value}")'
        dml(query)

    def read(table):
        query = f'SELECT * FROM {table}'
        print(dql(query))

    def update(table, update_new_value, update_where, where_value):
        query = f'UPDATE {table} SET valor = {update_new_value} WHERE {update_where} = "{where_value}"'
        dml(query)

    def delete(table, campo, valor_campo):
        query = f'DELETE FROM {table} WHERE {campo} = "{valor_campo}"'
        dml(query)


CRUD.create(table, update_new_value, update_where, where_value )
#CRUD.read(table)
CRUD.update(table, update_new_value, update_where, where_value )
#CRUD.delete(table, campo, valor)