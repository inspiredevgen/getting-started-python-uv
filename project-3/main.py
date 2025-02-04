from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

@main.route("/")
def index():
    #return render_template("login.html")
    return {"status":"UP"}

@main.route('/profile')
def profile():
    return {"page": "profile"}