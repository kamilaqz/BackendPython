import mysql.connector

class Usuario:

    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'ouvidoria'
    )
    cursor = connection.cursor()

    def __init__(self):
        pass

    def setNomeEmail(self, nome, email):
        sql = 'INSERT INTO usuario (nome, email) values (%s, %s)'
        data = (nome, email)
        self.cursor.execute(sql, data)
        self.connection.commit()

    def addOcorrencia(self, texto, tipo):
        sql = 'INSERT INTO ocorrencia (texto, tipo) values (%s, %s)'
        data = (texto, tipo)
        self.cursor.execute(sql, data)
        self.connection.commit()

    def getOcorrencias(self, tipo):
        sql = 'SELECT * FROM ocorrencia WHERE tipo = (%s)'
        data = (tipo,)
        self.cursor.execute(sql, data)
        lista = self.cursor.fetchall()
        for item in lista:
            print(item[0],' - ', item[1])

      
    def deleteOneOcorrencia(self, id):
        sql = 'DELETE FROM ocorrencia WHERE id = %s'
        data = (id, )
        self.cursor.execute(sql, data)
        self.connection.commit()

    def deleteAll(self):
        sql = 'DELETE FROM ocorrencia'
        self.cursor.execute(sql)
        self.connection.commit()

   
    def quit(self):
        self.cursor.close()
        self.connection.close()


