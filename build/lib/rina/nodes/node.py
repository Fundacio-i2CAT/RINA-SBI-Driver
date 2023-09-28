
class RinaNode():
    def __init__(self, portId, maName, systemId):
        self.portId = portId
        self.maName = maName
        self.systemId = systemId

    @property
    def PortId(self):
        return self.portId

    @property
    def MaName(self):
        return self.maName

    @property
    def SystemId(self):
        return self.systemId

    def printRinaNode(self):
        print("System Id: "+self.systemId+", MA Name: "+self.maName+", PortId: "+self.portId)



class RinaCoreNode():
    def __init__(self, url, maName, role, systemId):
        self.url = url
        self.role = role
        self.maName = maName
        self.systemId = systemId

    @property
    def Url(self):
        return self.url

    @property
    def Role(self):
        return self.role

    @property
    def MaName(self):
        return self.maName

    @property
    def SystemId(self):
        return self.systemId

    def printRinaCoreNode(self):
        print("System Id: "+self.systemId+", MA Name: "+self.maName+", role: "+self.role)