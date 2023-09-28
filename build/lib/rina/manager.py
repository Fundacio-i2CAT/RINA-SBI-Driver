from ast import ImportFrom
import functools
from pipes import Template
import socket
import sys


from rina.operations.system import ListSystem
from rina.operations.difs import CreateDif, DestroyDif
from rina.operations.ipcps import CreateIpcp, DestroyIpcp


OPERATIONS = {
    "list_systems":ListSystem,
    "create_dif":CreateDif,
    "create_ipcp": CreateIpcp,
    "destroy_dif": DestroyDif,
    "destroy_ipcp": DestroyIpcp,
} 




class RinaManager(object):

    def __init__(self, path_local_socket, path_templates):
        self.local_socket = path_local_socket
        self.templates = path_templates
        self.version = None
        self.listRinaNodes = []
        self.session = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    def __enter__(self):
        return self

    def __exit__(self):
        self.close_session()

    def execute(self, cls, *args, **kwds):
        return cls(self.session, self.listRinaNodes, self.templates).request(*args,**kwds)
    
    def __getattr__(self,method):
        if method in OPERATIONS:
            return functools.partial(self.execute, OPERATIONS[method])
    
    def path_templates(self,path_templates):
        self.templates = path_templates

    def connect(self):
        try:
            self.session.connect(self.local_socket)
        except Exception as e:
            print('Failed to connect to %s: %s' % (self.local_socket, e))
            quit(1)


