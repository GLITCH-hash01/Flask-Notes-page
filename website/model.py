from . import db #importing db=SQlAlchemy from website module 
from flask_login import UserMixin
from sqlalchemy.sql import func


#Note Database Structures

#id email date userid

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

#User database structure

#id email password firstname notes

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    notes=db.relationship('Note')



