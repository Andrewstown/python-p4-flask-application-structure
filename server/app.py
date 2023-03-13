from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

url = '/<string:username>'

@app.route(url)
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)