from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from app.database import init_db

app = Flask(__name__)

""" 
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///database.db'
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

def create_database(app):  
    print("Inside 'create_database'")
    if not path.exists('instance/baza_de_date.db'):
        with app.app_context():
            db.create_all()
            print('Database created!')
    else:
        print('Database already exists.')   
db.init_app(app)
create_database(app) """

init_db()