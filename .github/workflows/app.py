# This code is modified to check linter in this file
from flask import Flask, render_template
app = Flask(__name__)

print("test")
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
