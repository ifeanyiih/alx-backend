#!/usr/bin/env python3
"""Setup a basic Flask app with template.
Instantiate a Babel object.
"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Mapping, Dict, List, Union

app: Flask = Flask(__name__)
babel: Babel = Babel(app)
users: Mapping = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(ID: int) -> Union[Dict, None]:
    """Returns a user dictionary
    or None"""
    if users.get(ID):
        return users[ID]
    return None


class Config(object):
    """Configuration class
    Class will serve as configuration for
    the flask app object"""
    LANGUAGES: List[str] = ["en", "fr"]
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


@babel.timezoneselector
def get_timezone() -> str:
    """determines the timezone"""
    timezone = request.args.get('timezone')
    login_as = request.args.get('timezone')
    user = None
    if login_as:
        user = get_user(int(login_as))
    if timezone:
        try:
            check = pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError as e:
            return app.config['BABEL_DEFAULT_TIMEZONE']
    if user['timezone']:
        try:
            check = pytz.timezone(user['timezone'])
            return user['timezone']
        except pytz.exceptions.UnknownTimeZoneError as e:
            return app.config['BABEL_DEFAULT_TIMEZONE']
    return app.config['BABEL_DEFAULT_TIMEZONE']


@babel.localeselector
def get_locale() -> str:
    """determines the best match
    with supported languages"""
    locale = request.args.get('locale')
    login_as = request.args.get('login_as')
    user = None
    if login_as:
        user = get_user(int(login_as))
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if user and user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    if request.accept_languages:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route("/")
def home() -> str:
    """home route
    This is the root of the application"""
    return render_template('7-index.html')
