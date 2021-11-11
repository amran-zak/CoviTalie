# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask,render_template

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
#app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
    return "Hello World!"


@app.route('/index/')
def index1():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
