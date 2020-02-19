from flask import Flask, render_template,request,session, url_for


import json
import urllib.request


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("home.html")


@app.route("/story", methods=['GET','POST'])
def other():
    return render_template("story.html")


@app.route("/home", methods=['GET','POST'])
def another():
    return render_template("home.html")







if __name__ == '__main__':
    app.run(debug=True)