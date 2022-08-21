from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# let flask recognize that there is a database.
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY'] = 'c380dcafba240df1cf4ad02f'

db = SQLAlchemy(app)

from market import routes