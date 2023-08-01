#!/usr/bin/env python3
"""Setup a basic Flask app with
template"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """home route"""
    return render_template('0-index.html')
