# On day 66, we create an API that serves data on cafes with wifi and good coffee. Today, you're going to use the data from that project to build a fully-fledged website to display the information.
#
# Included in this assignment is an SQLite database called cafes.db that lists all the cafe data.
#
# Using this database and what you learnt about REST APIs and web development, create a website that uses this data. It should display the cafes, but it could also allow people to add new cafes or delete cafes.
#
# For example, this startup in London has a website that does exactly this:
#
# https://laptopfriendly.co/london
# has some css, bootstrap and google api, side tabs
# middle tab shows the coffee place

import sqlite3
from flask import Flask, jsonify, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import connexion
import requests
from flask import abort

# app = connexion.App(__name__, specification_dir='./')
# app.add_api('swagger.yml')
#
#
# con = sqlite3.connect('673 [assignment_file] Cafe and Wifi Website.db')
# cur = con.cursor()
# cur.execute('SELECT * FROM cafe')
# cafe = cur.fetchall()
#
#
# columns = [
#     ''
# ]
# for person_data in  coloum:
#     insert_cmd = f'INSERT INTO cafe VALUES ({person_data})'
#     conn.execute(insert_cmd)
#
# create_table_cmd = f"CREATE TABLE Cafe and Wifi Website ({','.join(columns)})"
# con.execute(create_table_cmd)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///673 [assignment_file] Cafe and Wifi Website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

def read_all():
    people = Cafe.query..all()
    return cafe_schema.dump(cafe)


@app.route('/')
def home():
    return render_template('home.html',content=[Cafe])

@app.route('/')
def welcome_page():
    return render_template('index.html')

@app.route(/<name>)
def user(name):
    return f'Welcome Back {name}!'

@app.route('/admin')
def admin():
    return redirect(url_for('user', name='Admin!'))

if __name__ === '__main__':
    app.run(debug=True)
