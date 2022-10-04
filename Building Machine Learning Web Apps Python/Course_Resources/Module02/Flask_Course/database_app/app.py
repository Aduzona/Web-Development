from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/database/users.db'
db = SQLAlchemy(app)

# Create A Class Model as A Schema for Database
class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	firstname = db.Column(db.String(50))
	lastname = db.Column(db.String(50))
	email = db.Column(db.String(80))
	message = db.Column(db.String(500))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/adduser',methods=['GET','POST'])
def adduser():
	if request.method == 'POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		email = request.form['email']
		message = request.form['message']

		# Adding Data To Database
		user = User(firstname=firstname,lastname=lastname,email=email,message=message)
		db.session.add(user)
		db.session.commit()
	return 'Your Firstname is ' + firstname + 'Your Email is ' + email


# Showing Data Inside DataBases
@app.route('/allusers')
def allusers():
	userslist = User.query.all()
	return render_template('results.html',userslist = userslist)


# Showing Individual Data via Dynamic URL Query
@app.route('/profile/<firstname>')
def profile(firstname):
	user = User.query.filter_by(firstname=firstname).first()
	return render_template('profile.html',user=user)

	

if __name__ == '__main__':
	app.run(debug=True)