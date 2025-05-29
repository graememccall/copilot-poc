class Game:
    def __init__(self, id, title, genre, release_year):
        self.id = id
        self.title = title
        self.genre = genre
        self.release_year = release_year

    def create(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO games (title, genre, release_year) VALUES (%s, %s, %s)", 
                       (self.title, self.genre, self.release_year))
        db_connection.commit()
        cursor.close()

    def update(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("UPDATE games SET title=%s, genre=%s, release_year=%s WHERE id=%s", 
                       (self.title, self.genre, self.release_year, self.id))
        db_connection.commit()
        cursor.close()

    def delete(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("DELETE FROM games WHERE id=%s", (self.id,))
        db_connection.commit()
        cursor.close()