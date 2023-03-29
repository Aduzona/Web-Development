from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint

#from dataclasses import dataclass
#from flask_migrate import Migrate
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)
#migrate = Migrate(app, db)


class Products(db.Model):
    id: int
    title: str
    image: str

    #Autoincrement is false because the product will be created in Django app
    '''
    This product is different form product from django app, because we don't have likes here.
    Thus different type of same thing.
    
    
    This app will catch the event from rabbitmq it will create
    the product, when we create the product, we don't want id to be autoincrement because
    the id  will be different than the django app.
    
    If we want the same id, then autoincrement=False, then insert directly the id as
    it is from the django app.
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

#@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    #user_id and product_id has to be unique.
    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')