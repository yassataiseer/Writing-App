from flask import Flask, render_template,request,session, url_for
import json
import urllib.request
import sqlite3 
import csv
import openpyxl
import pandas as pd 
conn = sqlite3.connect('data1.db', check_same_thread=False) 
c = conn.cursor() 
c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Username TEXT , Password TEXT)') 
app = Flask(__name__)


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
    username = request.form['username']
    password = request.form['pascode']
    c.execute("INSERT INTO RecordONE (Username, Password) VALUES(?, ?)", (username, password)) 
    c.execute("SELECT * FROM RecordONE ")
    rows = c.fetchall()
    for row in rows:
        if row[0]==username:
            return 'this Userame is already used please try anotherone'
        else:
            conn.commit() 
            return render_template("home.html", username = username, password=password)


@app.route("/login101", methods=['POST'])
def login101():
    username = request.form['username1']
    password = request.form['pascode1']
    print(username)
    c.execute("SELECT * FROM RecordONE ")
    rows = c.fetchall()
    for row in rows:
        if row[0]==username and row[1] ==password:
            return render_template("home.html")
    
    return "Invalid creds"

if __name__ == '__main__':
    app.run(debug=True)