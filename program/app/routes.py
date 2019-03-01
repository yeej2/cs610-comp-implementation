from app import app
from flask import render_template
from app.forms import LoginForm
from flask import Flask, render_template, redirect, url_for, request

# ...


@app.route('/')
def FUN_root():
    return render_template("index.html")

@app.route('/information/')
def FUN_info():
    return render_template("information.html")

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
