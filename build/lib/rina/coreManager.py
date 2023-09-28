import functools
from ast import ImportFrom

from rina.operations.system import  AddSystem, ListSystemCore
from rina.operations.difs import CreateDifCore


OPERATIONS = {
    "add_system": AddSystem,
    "list_systems": ListSystemCore,
    "create_dif": CreateDifCore # create_l2VPN  / destroy_l2VPN
} 


class RinaCoreManager(object):

     def __init__(self):
        self.version = None
        self.listRinaNodes = []
    
     def execute(self, cls, *args, **kwds):
        return cls(self.listRinaNodes).request(*args,**kwds)
    
     def __getattr__(self,method):
        if method in OPERATIONS:
            return functools.partial(self.execute, OPERATIONS[method])

