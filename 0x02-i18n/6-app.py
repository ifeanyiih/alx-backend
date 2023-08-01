#!/usr/bin/env python3
"""Setup a basic Flask app with template.
Instantiate a Babel object.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Mapping, Dict

app = Flask(__name__)
babel = Babel(app)
users: Mapping = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(ID: int) -> Dict:
    """Returns a user dictionary
    or None"""
    if users.get(ID):
        return users[ID]
    return None


class Config(object):
    """Configuration class
    Class will serve as configuration for
    the flask app object"""
    LANGUAGES: LIST[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)


@app.before_request
def before_request() -> None:
    """Function to be executed before
    any request"""
    login_as = request.args.get('login_as')
    if login_as:
        g.user = get_user(int(login_as))


@babel.localeselector
def get_locale() -> str:
    """determines the best match
    with supported languages"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    if request.accept_languages:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route("/")
def home() -> str:
    """home route
    This is the root of the application"""
    return render_template('6-index.html')
