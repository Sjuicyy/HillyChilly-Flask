from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "HillyChilly"

mysql = MySQL(app)


@app.route('/header')
def header():
    return render_template("headerfooter.html")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/vacationbundle")
def vacationbundle():
    return render_template("vacationbundle.html")


@app.route("/premiumtour")
def premiumtour():
    return render_template("premiumtour.html")


@app.route("/blogs")
def blogs():
    return render_template("blogs.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/postdemo")
def postdemo():
    return render_template('postdemo.html')



@app.route('/message', methods = ['POST'])
def message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        id1='0'
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO Messages
        VALUES(%s,%s,%s,%s)''',(name,email,message,id1))
        mysql.connection.commit()
        cursor.close()
        return f"Data added succesfully!!"


 
@app.route('/signup', methods = ['POST'])
def signup():
    if request.method == 'POST':
        id1='0'
        name = request.form['email']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO Signup VALUES(%s,%s)''',(id1,name))
        mysql.connection.commit()
        cursor.close()
        return f"Data added succesfully!!"

 
