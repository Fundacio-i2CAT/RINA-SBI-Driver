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
    "destroy_ipcp": DestroyIpcp
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

   # def list_systems(self):
  #      lines = issue_command(self.session, "list-systems")
 #       for line in lines[1:-1]:
 #           columns = line.split("|")
 #           node = RinaNode(columns[0], columns[1], columns[2])
 #           self.listRinaNodes.append(node)
 #           node.printRinaNode()
    
#        return self.listRinaNodes

#    def create_dif(self, systemId, path_descriptor_file):#
#        for node in self.listRinaNodes:
#            if (node.SystemId() == systemId):
#                cmd = "create-ipcp "+systemId+" "+path_descriptor_file
#                lines = issue_command(self.session, "create-ipcp")
#                print(lines)
#        print("error no systemId in the Dif")

