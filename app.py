from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'


@app.route('/', methods=['GET'])
def default_route():
    return '<h1>Hello world from Heroku</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
