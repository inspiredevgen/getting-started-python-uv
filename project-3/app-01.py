from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def root():
    return f'{'system': 'up'}'