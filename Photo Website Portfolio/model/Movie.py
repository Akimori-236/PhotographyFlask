from model.DatabasePool import DatabasePool

class Movie:
    
    # GET all movies
    @classmethod
    def getAllMovies(cls):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)
            sql = 'SELECT * FROM movie'
            cursor.execute(sql)
            allUsers = cursor.fetchall()
            return allUsers
        finally:
            dbConn.close()
            print('Connection released')
            
            
            
    # INSERT new movie
    @classmethod
    def insertMovie(cls, jsonMovie):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)
            sql = "INSERT INTO movie(name, description, releaseDate, imageURL, genreID) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql,(jsonMovie['name'], jsonMovie['description'], jsonMovie['releaseDate'], jsonMovie['imageURL'], jsonMovie['genreID']))
            dbConn.commit()                 # to commit changes to the database
            rows = cursor.rowcount          # returns number of changed rows
            return rows
        finally:
            dbConn.close()
            print("Connection released.")


    
    # SEARCH movies by substring
    @classmethod
    def getMoviesBySubstring(cls, substring):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)
            sql = "SELECT * from movie WHERE name LIKE concat('%', %s, '%')"
            cursor.execute(sql,(substring,))
            movies = cursor.fetchall()
            return movies
        finally:
            dbConn.close()
            print('Connection released')