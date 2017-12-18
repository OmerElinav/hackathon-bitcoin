from flask import Flask
from flask import render_template
from functools import wraps
from flask import request, Response

app = Flask(__name__)


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        return f(*args, **kwargs)

    return decorated


@app.route('/')
@requires_auth
def hello_world():
    print request.authorization['username']
    return render_template('index.html', name=request.authorization["username"])


app.run(host='127.0.0.1')
