import os


class HostIP:

    def __init__(self):
        ip = os.getenv('APP_HOST')
        if ip == None:
            ip = '0.0.0.0'
        self.ip = ip
        return
