from app import app
from flask import Flask, request, jsonify, abort
import os
import sys
import random
import string
import json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# create database url
basedir = os.path.abspath(os.path.dirname(__file__))
uri = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'user.db')
#print(uri)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# ma = Marshmallow(app)
# print(db)

# user model
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(32))
    def __init__(self, id):
        self.id = id
        self.key = randomString(random.randint(16, 32))

# generate a random number between 16 and 32
def randomString(strLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(strLength))

db.create_all()

# api call
@app.route('/user/<id>', methods=['POST'])
def addUser(id):
    if not id:
        abort(400, 'invalid id')
    else:
        data = {}
        # get port number
        data['port'] = f"{os.getpid()}"
        # check if user id already in the table
        curUser = db.session.query(user).filter(
            user.id == id
        ).first()
        if curUser:
            data['key'] = curUser.key
        else:
            # if new id, add to the table
            newUser = user(id)
            db.session.add(newUser)
            db.session.commit()
            data['key'] = newUser.key

    return jsonify(data), 200



@app.route('/', methods=['GET'])
def index():
    return f"Hello from {os.getpid()}"

