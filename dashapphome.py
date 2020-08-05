from flask import Flask

dashapp = Flask(__name__)


@dashapp.route("/")
def h():
    return '<h1 align="center">Dashapp in $/dashapp folder</h1>'


if __name__ == "__main__":
    dashapp.run()
