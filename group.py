from functions import *
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
    def removeMember(self,user):
        self.members.pop(user)

    def sendMessage(self,message):
        if(message["receiver"].active):
            if(checkMessage(message)):
                message["receiver"].messageBox.push(message)
            else:
                raise Exception("Malformed Message")
        else:
            raise Exception("Inactive User")
        return True
    def post(self):
        message = input("Digite a mensagem: ")
        for subscriber in self.members.values():
            self.sendMessage({"sender": self, "receiver": subscriber, "body": message})
