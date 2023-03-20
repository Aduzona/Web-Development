from flask import Flask,render_template,request,redirect, url_for,flash
from database import Book, connect_db

app = Flask(__name__)

app.config['SECRET_KEY']='3324199530042770d5a50abc'

@app.route('/')
def index():
    books = Book.select_books()
    return render_template('index.html', books=books)

@app.route('/add/', methods =['POST'])
def insert_book():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        book = Book(title=title, author=author, price=price)
        book.insert_book()
        flash("Book added successfully")
        return redirect(url_for('index'))
    
@app.route('/update/', methods=['POST'])
def update():
    if request.method == "POST":
        id = request.form['id']
        id=int(id)
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        book = Book.select_book_by_id(id)
        book.title = title
        book.author = author
        book.price = price
        book.update_book()
        flash("Book is updated")
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/', methods = ['GET', 'POST'])
def delete(id):
    book = Book.select_book_by_id(id)
    book.delete_book()
    flash("Book is deleted")
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)
