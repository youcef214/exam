"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from imperios import app
from flaskext.mysql import MySQL
from flask import request
import pymysql


mysql = MySQL(app, prefix='mysql', host='localhost', user='root', passwd='', db='imperio',autocommit=True,cursorclass=pymysql.cursors.DictCursor)
con = mysql.connect()
cursor = con.cursor()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/api/attack', methods=['POST'])
def attack():
    try:
        cursor.execute('insert into actions (user_id, typo) values ('+request.form['user_id']+', 1)')
        con.commit()
        print('the user: ' + request.form['user_id'] + ' attacks')
        return '',200
    except Exception as e:
        return '',500

@app.route('/api/defend', methods=['POST'])
def defend():
    try:
        cursor.execute('insert into actions (user_id, typo) values ('+request.form['user_id']+', 0)')
        con.commit()
        print('the user: ' + request.form['user_id'] + ' defends')
        return '',200
    except:
        return '',500

