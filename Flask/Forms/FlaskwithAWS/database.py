import psycopg2


def connect_db():
    connection = psycopg2.connect(host="localhost",port="5432",database="flaskaws",user="postgres",password="uvugaBaj21")
    cursor = connection.cursor()
    return connection,cursor

'''
cursor.execute("""
  CREATE TABLE Book (
    id serial PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    price Float NOT NULL
  );
""")
'''
#Insert
def insert_book(title,author,price):
    connection,cursor=connect_db()
    SQL="INSERT INTO book (title,author,price) values(%(title)s,%(author)s,%(price)s);"
    data={
        'title':title,
        'author':author,
        'price':price
    }
    cursor.execute(SQL,data)
    connection.commit()

#select
def select_book():
    connection,cursor=connect_db()
    cursor.execute("select * from book  ORDER BY id")
    book_data=cursor.fetchall()
    connection.commit()
    return book_data
    #for book in book_data:
        #print(book[1])#get title
    #connection.commit()

#update
def update_book():
    connection,cursor=connect_db()
    update_query = "UPDATE book SET title = %s WHERE id = %s"
    cursor.execute(update_query,('updated',1))
    connection.commit()

#delete
def delete_book():
    connection,cursor=connect_db()
    delete_query= "delete from book where id=%s"
    cursor.execute(delete_query,(1,))
    connection.commit()


def close_connection():
    connection,cursor=connect_db()
    connection.close()
    cursor.close()