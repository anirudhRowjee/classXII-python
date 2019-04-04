# linked list


class LinkedList:

    def __init__(self, name):
        self.name = name

    def addElement(self):
        return LinkedListElement(self)

class LinkedListElement(LinkedList):

    def __init__(self, value, preceding):
        self.parent = LinkedList
        self.value = value
        self.preceding = preceding

    def changeValue(self, new):
        self.value = new

    def showPrevious(self):
        print(self.preceding)
    
        
        
