from flask import Flask, render_template,request,session, url_for
import json
from flask_sqlalchemy import SQLAlchemy
import urllib.request
import sqlite3 
import csv
import openpyxl
import pandas as pd 

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db= SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.Text)
    Password = db.Column(db.Integer)
@app.route("/")
def index():
    print('1')
    return render_template("home.html")


@app.route("/story", methods=['GET','POST'])
def other():
    print('2')
    return render_template("story.html")


@app.route("/home", methods=['GET','POST'])
def another():
    print('3')
    return render_template("home.html")



@app.route("/yourstories", methods=['GET','POST'])
def anotherone():
    print('4')
    return render_template("storypage.html")

@app.route("/login", methods=['GET','POST'])
def login():
    print('5')
    return render_template("login.html")



@app.route("/signup", methods=['GET','POST'])
def signup():
    print('6')
    return render_template("signup.html")

@app.route("/story20", methods=['POST'])
def values():
    print('4')
    title= request.form['title']
    genres= request.form['genres']
    date = request.form['birthday']
    story = request.form['story']
    name = request.form['name']
    with  open("story.csv","a")as file:
        writer = csv.writer(file)
        writer.writerow([title , genres, date, story,name])       
        print(file)
        file.close()
    items = title,genres,date,story,name
    print(items[0])
    return render_template("home.html",items=items)

@app.route("/sign", methods=['POST'])
def sign():
    print('11111')
    username = request.form['username']
    password = request.form['pascode']
    print(username)
    user = User(Username=username, Password=password)
    
    user1 = User.query.filter_by(Username=username).first()
    print(username)

    if user1 is not None or username==''or password=='':
            return 'this Userame is already used please try anotherone or you have left a passage blank'
    else:
        db.session.add(user)
        db.session.commit()
        return render_template("home.html", username = username, password=password)


@app.route("/login101", methods=['POST'])
def login101():
    username = request.form['username1']
    password = request.form['pascode1']
    print(username)
    existing_user = User.query.filter_by(Username=username).first()
    pasword_checker = User.query.filter_by(Password=password).first()
    if existing_user is not None or pasword_checker is not None or username==''or password=='' :
        return render_template("home.html")
    else:
        return "Invalid creds"

if __name__ == '__main__':
    app.run(debug=True)