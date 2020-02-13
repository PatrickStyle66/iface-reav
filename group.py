class group:
    def __init__(self,name,desc,owner):
        self.owner = owner
        self.name = name
        self.desc = desc
        self.members = dict()

    def addMember(self,userInst):
        if(userInst.active):
            self.members[userInst.username] = userInst
            userInst.groups[self.name] = self
        else:
            raise Exception("Inactive User")