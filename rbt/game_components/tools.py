#This class represents the tools

class Tool():

    def __init__(self,id, type, owner):
        self.id = id
        self.type = type
        self.owner = owner

    def getState(self):
        return {
            'id': self.id,
            'type': self.type,
            'owner': self.owner
        }

