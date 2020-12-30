from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from waitress import serve
from pw_expire_list import Exec

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def hello_world():
    context = {
        'title': 'Home'
    }
    return render_template('home.html', context=context)

@app.route('/pw-expire-list')
def expirelist():
    elist = Exec()
    context = {
        'title': 'pw-expire-list',
        'data': elist.data
    }
    return render_template('pw-expire-list.html', context=context)

my_logger = None

if __name__ == '__main__':
    import os

    hostIP = os.environ.get('APP_HOST')
    if hostIP == None:
        hostIP = '0.0.0.0'

    portNum = os.environ.get('APP_PORT')
    if portNum == None:
        portNum = 5000

    serve(app, host=hostIP, port=portNum)