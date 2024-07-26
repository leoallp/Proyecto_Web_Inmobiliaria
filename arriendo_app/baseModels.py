from django.db import connection
"""
def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()
    return row
"""
#metodos genericos que permiten realizar consultas sql
class BaseModel:
    def executeQuery(self,sql,parametros=None):
        #obtenemos un objeto cursor que nos entrega conexion.
        cursor = connection.cursor()
        #with connection.cursor() as cursor:
        cursor.execute(sql, parametros if parametros is not None else [])
        print(cursor.description) #data que tenemos como respuesta
        data = cursor.description #recorrer la data
        #retornar lista[dicc]
        row = cursor.fetchone()
        return row



























