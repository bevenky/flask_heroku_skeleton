import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

if 'SECRET_KEY' in os.environ:
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
else:
    app.config['SECRET_KEY'] = 'this_should_be_configured'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
