import os


class IPCheck:

    def __init__(self, ip):
        self.ip = ip
        self.admin_mask = os.environ.get('APP_ADMIN_NET')
#        self.admin_mask = os.getenv('APP_ADMIN_NET')
        self.local_mask = '127.0.0.1'
        return

    @property
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

    @property
    def isLocal(self):
        if self.ip == self.local_mask:
            result = True
        else:
            result = False
        return result
