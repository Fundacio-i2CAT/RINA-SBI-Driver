from rina.operations.base import *
from rina.nodes.node import RinaNode

from rina.operations.utils import *

class CreateDif(Base):

    def request(self, difDescriptorFile):
        cmd = "create-dif "+self.template+"/"+difDescriptorFile
        print(cmd)
        lines = issue_command(self.session, cmd)


        return 0


class DestroyDif(Base):
    def request(self, difName):
        cmd = "destroy-dif "+difName
        print(cmd)
        lines = issue_command(self.session, cmd)

        return 0