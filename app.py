from flask import Flask
from flask_cors imoprt CORS


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
CORS(app)

@app.route('/', methods=['GET'])
def default_route():
    return '<h1>Hello world from Heroku</h1>'
