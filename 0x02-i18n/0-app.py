#!/usr/bin/env python3
""""""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home() -> str:
    """home route"""
    return render_template('0-index.html')
