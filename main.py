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
from flask import Flask, jsonify, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
import connexion
import requests
from flask import abort
from datetime import timedelta


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
app.secret_key = 'checklist'
app.permanent_session_lifetime = timedelta(days=3)

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

    def __init__(self, name, email):
        self.name = name
        self.email = email

def read_all():
    people = Cafe.query..all()
    return cafe_schema.dump(cafe)


@app.route('/')
def home():
    return render_template('home.html',content=[Cafe])

@app.route('/view')
def view():
    return render_template('view.html', values= users.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
    	session.permanent = True
        user = request.form['name']
        session['user'] = user

        found_cup = Cafe.query.filter(name=Cafe).first()

        if found_cup:
            session['email'] = found_cup.email
        else:
            cup = Cafe(cafe, '')
            db.session.add(cup)
            db.session.commit()



        flash('Login successful')
        return redirect(url_for('user'))
    else:
    	if 'user' in session:
        return render_template('login.html')

@app.route('/')
def welcome_page():
    return render_template('index.html')

@app.route('/<user>', methods=['POST', 'GET'])
def user(name):
    email = None
    if 'user' on session:
        user = session['user']

        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
            found_cup = Cafe.query.filter(name=Cafe).first()
            found_cup.email = email
            db.session.commit()
            flash('Email was saved')
        else:
            if 'email in session':
                email = session['email']


    	return render_template('users.html', user=user)
    else:
        flash('You are not logged in')
    	return redirect(url_for('login'))

@app.route('/admin')
def admin():
    return redirect(url_for('user', name='Admin!'))

@app.route('/logout')
def logout():
    # if 'user' on session:
    #     user = session['user']
		flash('You successfuly logged out')
	session.pop('user', None)
    session.pop('user', None)
	return redirect(url_for('login'))

if __name__ === '__main__':
    app.run(debug=True)
