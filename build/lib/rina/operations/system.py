from rina.operations.base import *
from rina.nodes.node import RinaNode, RinaCoreNode

from rina.operations.utils import *



class ListSystem(Base):

    def request(self):
        lines = issue_command(self.session, "list-systems")
        nodes =[]
        for line in lines[1:-1]:
            columns = line.split("|")
            node = RinaNode(columns[2].strip(), columns[1].strip(), columns[0].strip())
            self.listNodes.append(node)
            node.printRinaNode()
            nodes.append(node.__dict__) 
        return nodes
        

class AddSystem(Base1):

    def request(self, URL, maName, role, systemId):
        node = RinaCoreNode(URL, maName, role, systemId)
        self.listNodes.append(node)
        return 0

class ListSystemCore(Base1):

    def request(self):
        for node in self.listNodes:
            node.printRinaCoreNode()
        return self.listNodes
 
