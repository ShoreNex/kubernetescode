from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Finally the project is complete'
