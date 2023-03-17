from flask import Flask,render_template,request,redirect, url_for,flash
from database import select_book,connect_db

app =Flask(__name__)

app.config['SECRET_KEY']='3324199530042770d5a50abc'

@app.route('/')
def index():
    books=select_book()
    return render_template('index.html',books=books)

@app.route('/add/', methods =['POST'])
def insert_book():
    if request.method == "POST":
        title=request.form['title']
        author=request.form['author']
        price = request.form['price']
        connection, cursor = connect_db()
        cursor.execute("INSERT INTO book (title, author, price) VALUES (%s, %s, %s)", (title, author, price))
        connection.commit()
        connection.close()
        cursor.close()
        flash("Book added successfully")
        return redirect(url_for('index'))
    

@app.route('/update/',methods=['POST'])
def update():
    if request.method =="POST":
        id=request.form.get('id')
        title=request.form['title']
        author=request.form['author']
        price = request.form['price']
        connection, cursor = connect_db()
        update_query = "UPDATE book SET title = %s,author=%s,price=%s where id=%s"
        cursor.execute(update_query,(title,author,price,id))
        connection.commit()
        connection.close()
        cursor.close()
        flash("Book is updated")
        return redirect(url_for('index'))
    
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    #id = request.form.get('id')
    if id is not None:
        #id = int(id)

        connection, cursor = connect_db()
        delete_query="DELETE from book where id=%s"
        cursor.execute(delete_query,(id,))
        connection.commit()
        connection.close()
        cursor.close()
        flash("Book is deleted")
        return redirect(url_for('index'))

    else:
        flash("Error: No ID found in the form")
        return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)