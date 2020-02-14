from functions import *
class users:
    def __init__(self):
        self.users = dict()
        self.communities = dict()
        self.care = dict()
    def addCommunity(self,groupInst):
        if(not isIn(self.communities,groupInst.name)):
            self.communities[groupInst.name] = groupInst
        else:
            raise Exception("Community name already in use")

    def addUser(self,userInst,careInst):
        if(not isIn(self.users,userInst.username)):
            self.users[userInst.username] = userInst
            self.care[userInst.username] = careInst
        else:
            raise Exception("Username already in use.")
    def delete(self,userInst):
        self.users.pop(userInst.username)
        self.care.pop(userInst.username)

    def retrieveUser(self,name = "",login=False):
        if(isIn(self.users,name)):
            return self.users[name]
        matches = {uName: userInst for uName, userInst in self.users.items() if uName in name}
        if(matches and not login):
            return matches
        else:
            return None

    def retrieveCommunity(self,name):
        if(isIn(self.communities,name)):
            return self.communities[name]
        matches = {cName: commInst for cName, userInst in self.communities.items() if cName in name}
        if(matches):
            return matches
        else:
            return None

    def login(self,username,password):
        if(isIn(self.users,username)):
            return attempt(self.users[username].login(password))
        else:
            raise Exception("User doesn't exist")