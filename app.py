from flask import Flask
from flask import request
from flask import make_response
from flask import redirect


app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return 'Hello World, %s <br>' % user_agent

@app.route('/route/<name>')
def route(name):
    return '<h1>Hi, %s </h1>' % name

@app.route('/response')
def response():
    response = make_response('<h1>This doc carries a cookie!</h1>')
    response.set_cookie('answer','42');
    return response


@app.route('/redirecxt')
def redirecxt():
    return redirect('http://www.google.com')

if __name__ == '__main__':
    app.run(debug=True)


