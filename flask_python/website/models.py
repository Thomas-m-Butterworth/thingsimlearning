# This file stores our database models
from . import db    # Imports db from the current package
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    # Autolog date with func.now
    date =db.Column(db.DateTime(timezone=True), default=func.now())
    # Must pass a valid user ID
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):    # Create Object
    id = db.Column(db.Integer, primary_key = True)
    # Email is a string with a max-len of 150, and it must be unique
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
