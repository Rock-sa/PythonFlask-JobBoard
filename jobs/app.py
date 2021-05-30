#app = flask.objects(__name__)
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
