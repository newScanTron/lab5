from node import *


class DLL:
    def __init__(self):

        self.tail = Node("im the tail")
        self.head = self.tail

    def isEmpty(self):
        # Check if the head is empty
        return self.head is None

    def add(self, item):
        # Create a node for the new item
        temp = Node(item)
        # Set the next item to be the current head
        temp.setNext(self.head)
        # Set the new head to be the new item
        self.head = temp
        temp.setPrev(None)


#addmethod for index it will just be over loaded
    #also a sort of bad way to assign the self.tail
    def addIndex(self, item, index):
        count = 0
        temp = index
        current = self.head
        while count < self.length():
            while index <= count:
                current = current.getNext()
                prev = current.getPrev()
                count += 1
                if index is count:
                    temp = Node(item)
                    temp.setPrev(prev)
                    temp.setNext(current)
            current.setNext(None)
        # might make this print to see if it reasigns the tail with a different sring
            #than length
        self.tail = current

    def length(self):
        # Get the head node
        current = self.head
        count = 0
        # Loop until you get to a Node that has next item as None
        while current is not None:
            # Increment the count
            count += 1
            # Get the next node
            loopCurrent = current
            current = current.getNext()
            if current is None:
                self.tail = loopCurrent
        return count

    def search(self, item):
        # Get the head node
        current = self.head
        found = False
        stop = False
        # Loop until you get to a Node that has next item as None
        # and the item has not been found
        # and the flag doesn't say to stop
        while current is not None and not found and not stop:
            # See if the data of this item matches what we are looking for
            if current.getData() is item:
                found = True
            else:
                # if the current item is greater than what we
                # are looking for
                # Get the next node9
                current = current.getNext()
        return found
    def removeIndex(self, index):
        current = self.head
        count = 0
        while count < index:
            current = current.next()
        remover = current
        current.prev.setNext(current.getNext())
        return remover

    def remove(self, item):
        # Get the head node
        current = self.head
        previous = None
        found = False
        # While the node to remove hasn't been found
        while not found:
            # Check if this is the node
            if current.getData() == item:
                # The node to remove was found
                found = True
            else:
                # Set the previous to be the previous node
                previous = current
                # Get the next node as the current
                current = current.getNext()
        # If the previous node was None
        if previous is None:
            # Set the head to be the node after the current
            self.head = current.getNext()
        else:
            # Set the next for the previous to be the one after the
            # current node (the current is being removed from the list)
            previous.setNext(current.getNext())

    def removeHead(self):
        removeReturn = self.head.getData()
        self.head = self.head.getNext()
        return removeReturn

    def removeTail(self):
        remove_return = self.tail.getPrev()
        self.tail = remove_return
        #return remove_return.getData()
        if self.length() is 0:
            return None
        e = self.tail.getPrev().data
        self.tail.next = Node("im now the tail")
        #print("what", e)
        return e

    def append(self, element):
        self.tail.data = element
        self.tail.next = Node("im a added null tail")
        tmp = self.tail
        self.tail = self.tail.next
        self.tail.prev = tmp

    def printList(self):
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()

