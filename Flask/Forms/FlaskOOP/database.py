from config import connect_db
#from config import psycopg2



class Book:
    def __init__(self, id=None, title=None, author=None, price=None):
        self.id = id
        self.title = title
        self.author = author
        self.price = price

    @classmethod
    def select_books(cls):
        connection, cursor = connect_db()
        cursor.execute("SELECT * FROM book ")
        books = [cls(*book) for book in cursor.fetchall()]
        connection.close()
        cursor.close()
        return books

    @classmethod
    def select_book_by_id(cls, id):
        connection, cursor = connect_db()
        cursor.execute("SELECT * FROM book WHERE id=%s", (id,))
        book = cls(*cursor.fetchone())
        connection.close()
        cursor.close()
        return book

    def insert_book(self):
        connection, cursor = connect_db()
        insert_query = "INSERT INTO book (title, author, price) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (self.title, self.author, self.price))
        connection.commit()
        connection.close()
        cursor.close()

    def update_book(self):
        connection, cursor = connect_db()
        update_query = "UPDATE book SET title = %s, author = %s, price = %s WHERE id = %s"
        cursor.execute(update_query, (self.title, self.author, self.price, self.id))
        connection.commit()
        connection.close()
        cursor.close()
    
    def delete_book(self):
        connection, cursor = connect_db()
        delete_query = "DELETE FROM book WHERE id = %s"
        cursor.execute(delete_query, (self.id,))
        connection.commit()
        connection.close()
        cursor.close()       
                                                                 
                                                                        
