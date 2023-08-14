from flask import Flask


from poetry_demo.linkedlists import ll_rest

app = Flask(__name__)

print('app name', __name__)

app.register_blueprint(ll_rest)


@app.route('/')
def index():
    return 'Hello, World!'
