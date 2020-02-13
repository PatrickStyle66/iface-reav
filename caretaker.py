class caretaker:
    def __init__(self,user):
        self.user = user
        self.history = []

    def LastEdit(self):
        m = self.user.save()
        self.history.append(m)

    def undo(self):
        m = self.history.pop()
        self.user.restore(m)