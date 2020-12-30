from os import path
from subprocess import Popen, PIPE
import json
from typing import Any, Union


class Exec:

    def __init__(self):
        self.data = []
        folder_path = path.dirname(path.abspath(__file__))
        full_path = path.join(folder_path, 'command.ps1')
        # cmd_string = self.build_cmd(full_path=full_path)
        self.data = self.do_cmd(script_path=full_path)
        self.rename_columns()

    def build_cmd(self, full_path):
        c = ''
        with open(full_path, 'r') as fp:
            line = fp.readline()
            while line:
                if line[0] == '#':
                    pass
                else:
                    c = c + line.replace('\n', '') + ';'
                line = fp.readline()

        c = c.replace('\"', '`')
        c = '"& {' + c + '}"'
        return c

    def do_cmd(self, script_path):
        pipe = Popen(['powershell.exe', '-File', script_path], stdout=PIPE)
        x = pipe.communicate()[0]
        data = json.loads(x)
        return data

    #
    # rename samaccountname to name
    # PasswordLastSet to lastset
    # DaysUntilExpire to days
    #
    def rename_columns(self):
        d = []
        for i in self.data:
            item = {
                'name': i['samaccountname'],
                'days': i['DaysUntilExpired']
            }
            d.append(item)
        self.data = []
        self.data = d
        return


