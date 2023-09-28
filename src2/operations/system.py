from rina.operations.base import *
from rina.nodes.node import RinaNode

from rina.operations.utils import *



class ListSystem(Base):

    def request(self):
        lines = issue_command(self.session, "list-systems")
        for line in lines[1:-1]:
            columns = line.split("|")
            node = RinaNode(columns[2].strip(), columns[1].strip(), columns[0].strip())
            self.listNodes.append(node)
            node.printRinaNode()
        return self.listNodes
        


