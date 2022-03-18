from model.DatabasePool import DatabasePool

class Genre:

    # GET all genres
    @classmethod
    def getAllGenres(cls):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)
            sql = 'SELECT * FROM genre'
            cursor.execute(sql)
            allGenres = cursor.fetchall()
            return allGenres
        finally:
            dbConn.close()
            print('Connection released')



    # INSERT new genre
    @classmethod
    def insertGenre(cls, jsonGenre):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)
            sql = "INSERT INTO genre(name, description) VALUES (%s, %s)"
            cursor.execute(sql,(jsonGenre['name'], jsonGenre['description']))
            dbConn.commit()                 # to commit changes to the database
            rows = cursor.rowcount          # returns number of changed rows
            return rows
        finally:
            dbConn.close()
            print("Connection released.")