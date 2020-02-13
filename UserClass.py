from functions import *
from messageBox import messageBox
class user:
    def __init__(self,active = False):
        self.attrs = dict()
        self.messageBox = messageBox()
        self.active = active
        self.friends = dict()
        self.requests = dict()
        self.groups = dict()

    def create(self,username,password,name):
        if(not reMatch(str(username),onlyLetters)):
            raise Exception("Invalid username")
        self.username = username
        self.password = hashPass(password)
        self.name = name
        self.active = True
        return(self)

    def delete(self):
        for friend in self.friends:
            friend.friends.pop(self.username)
        for key in self.__dict__.keys():
            self.__dict__[key] = None

    def login(self,password):
        if(self.active):
            if(self.password == hashPass(password)):
                return self
        else:
            raise Exception("Wrong Password")

    def addAttr(self,key,value,conf = False):
        if(reMatch(key,onlyLettersAndWhitespace) and reMatch(value,passwordPattern)):
            if key in self.attrs.keys():
                if(conf):
                    self.attrs[key] = value
                else:
                    raise Exception("Not Confirmed")
            else:
                self.attrs[key] = value
        else:
            raise Exception("Invalid string")
        return True

    def showAttrs(self):
        return self.attrs

    def addFriend(self,userInst):
        if(userInst.active):
            if(isIn(userInst.requests,self.username)):
                self.friends[userInst.username] = userInst
                userInst.requests.pop(self.username)
                userInst.friends[self.username] = self
                print("Vocês são amigos agora!")
            else:
                self.requests[userInst.username] = userInst
                print("Pronto! Convite enviado.")
        else:
            raise Exception("Inactive User")
        return True

    def sendMessage(self,message):
        if(message["receiver"].active):
            if(checkMessage(message)):
                message["receiver"].messageBox.push(message)
            else:
                raise Exception("Malformed Message")
        else:
            raise Exception("Inactive User")
        return True