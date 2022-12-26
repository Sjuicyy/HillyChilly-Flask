from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello():
#     return ('hello world')


@app.route('/header')
def header():
    return render_template("headerfooter.html")

@app.route("/premiumtour")
def premiumtour():
    return render_template("premiumtour.html")


@app.route("/vacationbundle")
def vacationbundle():
    return render_template("vacationbundle.html")

@app.route("/")
def home():
    return render_template("index.html")