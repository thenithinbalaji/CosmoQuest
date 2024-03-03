import pymongo, os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from bson import json_util
import json
import datetime
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = "vaishnave nithin"
database_name = "cosmoquest"

# loading env data
try:
	from dotenv import load_dotenv

	load_dotenv()
except Exception as err:
	print(err)

mongo_uri = "mongodb+srv://thenithinbalaji:wv9v9sspzZSAeCj@cosmoquest.o9ocbh2.mongodb.net/?retryWrites=true&w=majority&appName=Cosmoquest"
print(mongo_uri)

myclient = pymongo.MongoClient(mongo_uri)
dblist = myclient.list_database_names()

if database_name in dblist:
    print(f"The '{database_name}' database exists")
else:
    mydb = myclient[database_name]
    auth = mydb["auth"]

@app.route("/")
def home():
	if "user" in session:
		return render_template("home.html", login = "true")
	else:
		return render_template("home.html", login = "false")

@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("home"))
    else:
        if request.method == "GET":
            return render_template("login.html")
        else:
            email = request.form["email"]
            password = request.form["password"]

            client = pymongo.MongoClient(mongo_uri)
            db = client[database_name]
            collection = db["auth"]

            user = collection.find_one({"email": email, "password": password})

            if user is None:
                return redirect(url_for("login"))

            session["user"] = json.loads(json_util.dumps(user))
            return redirect(url_for("home"))

@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for("home"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if "user" in session:
        return redirect(url_for("home"))
    else:
        if request.method == "GET":
            return render_template("signup.html")
        else:
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            repassword = request.form["repassword"]
            
            if password != repassword:
                return redirect(url_for("signup"))

            client = pymongo.MongoClient(mongo_uri)
            db = client[database_name]
            collection = db["auth"]

            if collection.find_one({"email": email}) is not None:
                flash("Email already exists!", "danger")
                return redirect(url_for("signup"))

            collection.insert_one({
                "name": name,
                "email": email,
                "password": password
            })
            flash("Account created successfully!", "success")
            return redirect(url_for("login"))

@app.route("/mars", methods=["GET", "POST"])
def mars():
    if not request.args.get('date'):
        return render_template("mars.html")
    else:
        planet = "Mars"
        date = request.args.get('date')
        count = request.args.get('passengers')

        user_email = session.get('user')["email"]
        
        client = pymongo.MongoClient(mongo_uri)
        db = client[database_name]
        collection = db["auth"]

        collection.update_one({"email": user_email}, {"$push": {"tickets": {"planet": planet, "date": date, "passengers": count}}})

        user = collection.find_one({"email": session.get('user')["email"]})
        session["user"] = json.loads(json_util.dumps(user))

        return redirect(url_for("dash"))

@app.route("/moon", methods=["GET", "POST"])
def moon():
    if not request.args.get('date'):
        return render_template("moon.html")
    else:
        planet = "Moon"
        date = request.args.get('date')
        count = request.args.get('passengers')

        user_email = session.get('user')["email"]
        
        client = pymongo.MongoClient(mongo_uri)
        db = client[database_name]
        collection = db["auth"]

        collection.update_one({"email": user_email}, {"$push": {"tickets": {"planet": planet, "date": date, "passengers": count}}})

        user = collection.find_one({"email": session.get('user')["email"]})
        session["user"] = json.loads(json_util.dumps(user))

        return redirect(url_for("dash"))

@app.route("/jupiter", methods=["GET", "POST"])
def jupiter():
    if not request.args.get('date'):
        return render_template("jupiter.html")
    else:
        planet = "Jupiter"
        date = request.args.get('date')
        count = request.args.get('passengers')

        user_email = session.get('user')["email"]
        
        client = pymongo.MongoClient(mongo_uri)
        db = client[database_name]
        collection = db["auth"]

        collection.update_one({"email": user_email}, {"$push": {"tickets": {"planet": planet, "date": date, "passengers": count}}})

        user = collection.find_one({"email": session.get('user')["email"]})
        session["user"] = json.loads(json_util.dumps(user))

        return redirect(url_for("dash"))
        

@app.route("/saturn", methods=["GET", "POST"])
def saturn():
    if not request.args.get('date'):
        return render_template("saturn.html")
    else:
        planet = "Saturn"
        date = request.args.get('date')
        count = request.args.get('passengers')

        user_email = session.get('user')["email"]
        
        client = pymongo.MongoClient(mongo_uri)
        db = client[database_name]
        collection = db["auth"]

        collection.update_one({"email": user_email}, {"$push": {"tickets": {"planet": planet, "date": date, "passengers": count}}})

        user = collection.find_one({"email": session.get('user')["email"]})
        session["user"] = json.loads(json_util.dumps(user))

        return redirect(url_for("dash"))

@app.route("/dashboard")
def dash():
    if "user" in session:
        return render_template("dashboard.html", user = session["user"], travel = session["user"])
    else:
        return redirect(url_for("login"))

@app.errorhandler(404)
def not_found_error(error):
	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run(debug=True)