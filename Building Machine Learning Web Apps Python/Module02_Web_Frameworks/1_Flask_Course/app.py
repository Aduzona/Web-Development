from flask import Flask,render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy
# init app

app =Flask(__name__)

#DB
# Wrap app within sqlalchemy
db= SQLAlchemy(app)

# Configure the location where the data is stored
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///static/database/users.db'

# model schema that is used to build structure for database
class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String(50))
    lastname=db.Column(db.String(50))

# Route
@app.route('/')
def index():
    return 'Hello Data Science Optimizers'


# Adding HTML
@app.route('/home')
def home():
    return render_template('home.html')


# Adding predict
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        #putting the data inside the database
        single_user =User(firstname=firstname,lastname=lastname)
        db.session.add(single_user)
        db.session.commit()
    return render_template('home.html',firstname=firstname.upper(),lastname=lastname.upper())


#Retrieve data from database
@app.route('/allusers')
def allusers():
    userslist =User.query.all() #store everything inside userslist
    print(userslist)
    return render_template('results.html',userslist=userslist)

#Searching Databases
@app.route('/profile/<firstname>')
def profile(firstname):
    user =User.query.filter_by(firstname=firstname).first()
    return render_template('profile.html',user=user)

# Templating
@app.route('/about')
def about():
    mission ="Optimizing Data and ML Models"
    return render_template('about.html',mission=mission)

if __name__=='__main__':
    app.run(debug=True)# After developing, do debug=False