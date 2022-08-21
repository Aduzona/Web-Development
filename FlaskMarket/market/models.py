from market import db

# username and password
class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username =db.Column(db.String(length=30),nullable=False,unique=True)
    email_address= db.Column(db.String(length=50),nullable=False, unique=True)
    password_hash=db.Column(db.String(length=60),nullable=False)
    budget=db.Column(db.Integer(),nullable=False, default=1000)

    #Allow users to owns several items.
    #backref is backreference to user.
    #lazy=True allows sqlalchemy to grab in one shot.
    items=db.relationship('Item',backref='owned_user',lazy=True)

class Item(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30),nullable=False, unique=True)
    price = db.Column(db.Integer(),nullable=False, unique=True)
    barcode = db.Column(db.String(length=12),nullable=False, unique=True)
    description = db.Column(db.String(length=1024),nullable=False, unique=True)
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))# user.id relates with User class

    def __repr__(self):
        '''
        About __repr__
        https://www.educative.io/answers/what-is-the-repr-method-in-python
        '''
        return f'Item {self.name}'