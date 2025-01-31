from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/signup")
def signup():
    return {"page":"signup"}

@auth.route("/login")
def login():
    return {"page":"login"}

@auth.route("/logout")
def logout():
    return {"page":"logout"}