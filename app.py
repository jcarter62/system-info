from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from waitress import serve
from pw_expire_list import Exec
import os

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def root_route():
    context = {
        'title': 'Home'
    }
    return render_template('home.html', context=context)

@app.route('/not-authorized')
def not_auth():
    context = {
        'title': 'Not Authorized'
    }
    return render_template('not-authorized.html', context=context)


@app.route('/pw-expire-list')
def expirelist():
    elist = Exec()
    context = {
        'title': 'pw-expire-list',
        'data': elist.data
    }
    return render_template('pw-expire-list.html', context=context)

@app.before_request
def before_request():
    from utils import IPCheck
    r = request
    requested_path = request.full_path
    requested_path = requested_path.replace('?', '')
    print('path = ' + requested_path)
    if  requested_path[0:7] == '/static' or requested_path == '/' or requested_path == '/not-authorized':
        pass
    else:
        ip = r.remote_addr
        ip_check = IPCheck(ip)
        if not ip_check.authorized():
            return redirect('/not-authorized')

    return


my_logger = None

if __name__ == '__main__':
    from utils import HostIP

    hip = HostIP()
    serverip = hip.ip
    serverPort = hip.port

    msg = 'Server IP = {} and Port = {}'
    print(msg.format(serverip, serverPort))

    serve(app, host=serverip, port=serverPort)
