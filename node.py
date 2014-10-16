class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next

    def setPrev(self, new_prev):
        self.prev = new_prev