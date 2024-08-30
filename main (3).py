from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# staff only
@app.route('/private')
def index():
    return render_template("index.html")

# for getting into site
@app.route('/', methods=["POST"])
def login():
    return render_template("login.html")

@app.route('/registration')
def register():
    return render_template("register.html")

# main site
@app.route('/home', methods=["POST"])
def home():
    return render_template("home.html")

@app.route('/home/menu')
def menu():
    return render_template("menu.html")

@app.route('/home/order')
def order():
    return render_template("order.html")

@app.route('/home/order/order_details')
def order_details():
    return render_template("order_details.html")

@app.route('/home/feedback')
def feedback():
    return  render_template("feedback.html")

@app.route('/home/terms')
def terms():
    return render_template("TandC.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
