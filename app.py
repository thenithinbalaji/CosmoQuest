import os
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "vaishnave nithin"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/earth")
def earth():
    return render_template("earth.html")

@app.route("/mars")
def mars():
    return render_template("mars.html")

@app.route("/moon")
def moon():
    return render_template("moon.html")

@app.route("/jupiter")
def jupiter():
    return render_template("jupiter.html")

@app.route("/saturn")
def saturn():
    return render_template("saturn.html")

if __name__ == "__main__":
	app.run(debug=True)