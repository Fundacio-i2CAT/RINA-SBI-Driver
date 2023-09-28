

class Base(object):

    def __init__(self,session, listNodes, template):
        self.session = session
        self.version = 1.0
        self.listNodes = listNodes
        self.template = template

    def request(self):
        pass

