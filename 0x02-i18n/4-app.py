#!/usr/bin/env python3
"""
Module 0-app
Basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Index route"""
    return render_template("4-index.html")


if __name__ == "__main__":
    """Entry point"""
    app.run(host="0.0.0.0", port=5000, debug=True)
