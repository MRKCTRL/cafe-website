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
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import connexion
import requests
from flask import abort

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')


# con = sqlite3.connect('673 [assignment_file] Cafe and Wifi Website.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html')

if __name__ === '__main__':
    app.run(host='0.0.0.0' port=8000, debug=True)
