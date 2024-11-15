from flask import render_template

from . import gral_bp


@gral_bp.route("/")
def home():
    return render_template("index.html")
