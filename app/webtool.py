from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']  = 'National345'
app.config['MYSQL_DB'] = 'pace'

mysql = MySQL(app)


@app.route("/")
def home():
    return render_template('home.html')
    #return "Hello World!"

@app.route("/user_info")
def user_info():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM user_list"
    cursor.execute(sql)
    results = cursor.fetchall()

    return render_template('user_info.html', results=results)


    # if request.method == "POST":
    #     details = request.form
        
    #return "Please update your info."

@app.route("/products")
def products():
    return render_template("products.html")
    return "Please select a product."

@app.route("/creation")
def creation():
    return render_template('creation.html')

@app.route("/request_submitted")
def request_submitted():
    return render_template('request_submitted.html')

@app.route("/account", methods = ['GET','POST'])
def account():
    return render_template('account.html')

if __name__ == "__main__":
    app.run(debug=True)