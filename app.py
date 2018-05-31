#!/usr/bin/env python3
"""
This is the application file. It contains the main program and
is meant to be executed
"""


from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", text="Hello World")