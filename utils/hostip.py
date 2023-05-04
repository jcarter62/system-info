import os
from decouple import config

class HostIP:

    def __init__(self):
        self.ip = self.get_app_host()
        self.port = self.get_app_port()
        return

    def get_app_host(self):
        try:
            ip = config('APP_HOST')
        except:
            ip = None

        if ip is None:
            ip = '0.0.0.0'
        return ip

    def get_app_port(self):
        try:
            port = config('APP_PORT')
        except:
            port = None

        if port is None:
            port = 5000
        return port
