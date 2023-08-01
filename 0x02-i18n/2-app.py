#!/usr/bin/env python3
"""Setup a basic Flask app with template.
Instantiate a Babel object.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configuration class
    Class will serve as configuration for
    the flask app object"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home() -> str:
    """home route"""
    return render_template('1-index.html')
