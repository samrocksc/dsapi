from flask import Flask

from dsapi.linkedlists import ll_rest_v1
from dsapi.twosum import twosum_rest_v1


app = Flask(__name__)

print('app name', __name__)

app.register_blueprint(ll_rest_v1)
app.register_blueprint(twosum_rest_v1)


@app.route('/')
def index():
    return 'Hello, World!'
