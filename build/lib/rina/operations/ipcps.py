from rina.operations.base import *
from rina.nodes.node import RinaNode

from rina.operations.utils import *

class CreateIpcp(Base):

    def request(self, systemId, difDescriptorFile):
        # check if the systemId is in the RinaNode list
        # Check if the difDescriptorFile is on the template directory.
        cmd =  "create-ipcp "+systemId+" "+ self.template+"/"+difDescriptorFile
        lines = issue_command(self.session, cmd)
        words = lines[0].split()

        for word in words:
            if (word == "successfully"):

                print(lines[0])
                break  
            elif (word == "Error"):
                print("Error while creating Icpc in the system " + systemId)
                break


        return


class DestroyIpcp(Base):
    def request(self, systemId, ipcpId):
        cmd = "destroy-ipcp "+systemId+" "+ ipcpId
        lines = issue_command(self.session, cmd)
        words = lines[0].split()
        for word in words:
            if (word == "successfully"):
                print("Ipcp Destroyed succesfully")
                break  
            elif (word == "Error"):
                print("Error while destroying Icpc "+ipcpId+" in the system " + systemId)
                break
        return 0