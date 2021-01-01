import os


class IPCheck:

    def __init__(self, ip):
        self.ip = ip
        self.admin_mask = os.environ.get('APP_ADMIN_NET')
        self.local_mask = '127.0.0.1'
        return

    def location(self):
        location = ''
        if self.isLocal:
            location = location + 'local '
        if self.isAdmin:
            location = location + 'admin '
        return location

    def authorized(self):
        if self.isAdmin():
            return True
        if self.isLocal():
            return True
        return False

    def isAdmin(self):
        if self.admin_mask is None:
            result = False
        else:
            mlen = len(self.admin_mask)
            shortip = self.ip[0:mlen]
            result = False
            if self.admin_mask == shortip:
                result = True

        return result

    def isLocal(self):
        if self.ip == self.local_mask:
            result = True
        else:
            result = False
        return result
