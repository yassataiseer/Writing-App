from flask import Flask, render_template,request,session, url_for


import json
import urllib.request


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
    print('3')
    return render_template("storypage.html")


@app.route("/", methods=['POST'])
def values():
    print('4')
    title= request.form['title']
    genres= request.form['genres']
    date = request.form['birthday']
    story = request.form['story']
    name = request.form['name']

    return render_template("home.html",title=title,genres=genres,date=date,story=story,name=name)





if __name__ == '__main__':
    app.run(debug=True)