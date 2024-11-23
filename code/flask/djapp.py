''' sample flask project '''
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    ''' standard hello world app'''
    return ("hello world from pyproject")


if __name__ == "__main__":
    app.run()
