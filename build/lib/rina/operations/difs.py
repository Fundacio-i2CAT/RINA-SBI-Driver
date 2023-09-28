from rina.operations.base import *
from rina.nodes.node import RinaNode, RinaCoreNode

from rina.operations.utils import *

class CreateDif(Base):

    def request(self, difDescriptorFile):
        cmd = "create-dif "+self.template+"/"+difDescriptorFile
        lines = issue_command(self.session, cmd)
        words = lines[0].split()

        for word in words:
            if (word == "created"):
                print(lines[0])
                print(lines[1])
                break  
            elif (word == "Error"):
                print("Error while creating DIF")
                break


        return 0


class DestroyDif(Base):
    def request(self, difName):
        cmd = "destroy-dif "+difName
        print(cmd)
        lines = issue_command(self.session, cmd)
        words = lines[0].split()

        for word in words:
            if (word == "destroyed"):
                print(lines[0])
                print(lines[1])
                break  
            elif (word == "Error"):
                print("Error while destroying DIF")
                break

        return 0


class CreateDifCore(Base1):
    def request(self, systemId, sliceId):
        node = look_up_node(self.listNodes, systemId)

        if (node != 0):
            post_request(node, sliceId)
        