from model.DatabasePool import DatabasePool

class Photo:
    
    # GET all photos
    @classmethod
    def getAllPhotos(cls):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)
            sql = 'SELECT * FROM photo'
            cursor.execute(sql)
            allPhotos = cursor.fetchall()
            return allPhotos
        finally:
            dbConn.close()
            print('Connection released')
            
    # GET all scenery photos
    @classmethod
    def getPhotosFromGenre(cls, genre):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)
            sql = 'SELECT * FROM photo WHERE genre = %s'
            genre = tuple(genre)
            cursor.execute(sql, genre)
            allPhotos = cursor.fetchall()
            return allPhotos
        finally:
            dbConn.close()
            print('Connection released')
            
