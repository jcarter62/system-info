import os


class IPCheck:

    def __init__(self, ip):
        self.ip = ip
        self.admin_type = ''

        file_or_mask = os.environ.get('APP_ADMIN_NET')
        if file_or_mask.__contains__(os.sep):
            self.admin_type = 'file'
        else:
            self.admin_type = 'mask'

        if self.admin_type == 'mask':
            self.admin_mask = file_or_mask
        else:
            self.admin_list = self.load_admin_list(file_or_mask)

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
        if self.admin_type == 'mask':
            mlen = len(self.admin_mask)
            shortip = self.ip[0:mlen]
            result = False
            if self.admin_mask == shortip:
                result = True
        else: ## file
            result = False
            for msk in self.admin_list:
                mlen = len(msk)
                shortip = self.ip[0:mlen]
                if msk == shortip:
                    result = True
        return result

    def isLocal(self):
        if self.ip == self.local_mask:
            result = True
        else:
            result = False
        return result

    @staticmethod
    def load_admin_list(filename) -> list:
        admin_list = []
        with open(filename, mode='r') as f:
            for line in f:
                if line.__len__() > 5:
                    admin_list.append(line)
        return admin_list
