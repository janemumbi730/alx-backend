#!/usr/bin/env python3
"""
Module 0-app
Basic flask app
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
# Then instantiate the Babel object in your app.
# Store it in a module-level variable named babel.
babel = Babel(app)


class Config(object):
    """
    Language and timezone configuration class
    Use Config to set Babel's default locale ("en") and timezone ("UTC")
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Use that class as config for your Flask app
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Use request.accept_languages to determine the
    best match with our supported languages
    """
    local_e = request.args.get("locale", None)
    if local_e and local_e in app.config["LANGUAGES"]:
        return local_e

    if g.user:
        local_e = g.user.get("locale")
        if local_e in app.config["LANGUAGES"]:
            return local_e

    local_e = request.headers.get("locale", None)
    if local_e and local_e in app.config["LANGUAGES"]:
        return local_e

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Index route"""
    return render_template("6-index.html")


def get_user():
    """
    Returns a user dictionary or None if the ID cannot
    be found or if login_as was not passed.
    """
    user_id = request.args.get("login_as", None)
    if user_id is None:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """
    Uses the app.before_request decorator to make it be executed
    before all other functions.
    Uses get_user to find a user if any, and set it as a
    global on flask.g.user.
    """
    usr = get_user()
    g.user = usr


if __name__ == "__main__":
    """Entry point"""
    app.run(host="0.0.0.0", port=5000, debug=True)
