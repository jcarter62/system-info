from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from waitress import serve
from pw_expire_list import Exec
from ipcheck import IPCheck
import os

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def root_route():
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

@app.before_request
def before_request():
    r = request
    ip = r.remote_addr
    ip_check = IPCheck(ip)
    location = ''
    if ip_check.isLocal:
        location = location + 'local '
    if ip_check.isAdmin:
        location = location + 'admin '

    s = 'request ip = {}, {}'
    print(s.format(ip, location))
    return



my_logger = None

if __name__ == '__main__':
    from evars import HostIP

    hip = HostIP()
    serverip = hip.ip


#     hostIP = os.getenv('APP_HOST')
#     if hostIP == None:
#         hostIP = '0.0.0.0'
#         hostIP = '10.100.20.187'
#

    portNum = os.getenv('APP_PORT')
    if portNum == None:
        portNum = 5000

    serve(app, host=serverip, port=portNum)