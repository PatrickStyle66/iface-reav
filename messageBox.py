class messageBox:
    def __init__(self,messages = ()):
        self.messages = messages

    def push(self,message):
        self.messages.append(message)

    def peek(self):
        if(self.messages):
            return self.messages[-1]

    def list(self):
        return [(index,self.messages[index]) for index in range(len(self.messages))]