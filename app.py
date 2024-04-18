import os
from flask import Flask, render_template, redirect, url_for, request, session, make_response
import mysql.connector
from flask_session import Session
import json
import time

app = Flask(__name__, template_folder='Static/templates')
app.config["DEBUG"] = False
app.config["SECRET_KEY"] = "SUPERSECRETKEY" # os.getenv('FLASK_SECRET_KEY', 'default_secret_key')

# session persists even if browser is closed
app.config["SESSION_PERMANENT"] = True
# session persists even if server restarts
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',  # or 'Strict'
)

@app.route("/")
def index():
    # return render_template("index.html")
    if 'name' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    if 'name' not in session or session['name'] is None:
        return redirect('/')
    # return render_template("index.html")
    return render_template('dashboard.html')

# @app.route('/users/registration', methods = ['POST'])
# def register():
#     if request.method == 'POST':
#         data = request.get_json()
#         return data
#     else:
#         return "Bad Request", 400


@app.route("/login", methods=["POST", "GET"])
def login():
  # if form is submited
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if 'name' in session and session['name'] == username:
            return redirect('/dashboard')

        if authenticate(username, password):
            session['name'] = username  
            return redirect('/dashboard')
        else:
            return 'Login Failed'
        
    return render_template('login.html')

@app.route('/logout', methods=["GET", "POST", "DELETE"])
def logout():
    session.clear()  # Clear session data
    response = make_response('You have been logged out')
    response.set_cookie('session', '', expires=0)  # Delete session cookie
    return redirect('/')

# @app.route('/delete-user', methods=['POST'])
# def delete_user(user_id):
#     if request.method == 'POST':
#         data = request.get_json()
#         print (data)
#         return "this was a delete request"

def authenticate(username, password):
    # authentication logic
    if username == password:
        return False
    return True

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80)
