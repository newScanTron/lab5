from node import *

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        # Check if the head is empty
        return self.head == None

    def add(self, item):
        # Set the current node to be head
        current = self.head
        # This will be the previous node
        previous = None
        # Flag for when to stop looping
        stop = False
        
        # Loop while we haven't hit the end of the list
        # (i.e. current == None) and we are not being
        # told to stop by the flag
        while current != None and not stop:
            # If the data is greater than what we are adding
            if current.getData() > item:
                # Stop - the new item needs to go before current
                stop = True
            else:
                # Set previous to current node
                previous = current
                # Set current to be the next node
                current = current.getNext()

        # Create a node for the item we are adding
        temp = Node(item)

        # If previous is None, then we are adding at head
        if previous == None:
            # Set the next item to be the current head
            temp.setNext(self.head)
            # Set the new head to be the new item
            self.head = temp
        else:
            # Set the next node of the new node to be current
            temp.setNext(current)
            # Connect the previous node to the new node
            previous.setNext(temp)

    def length (self):
        # Get the head node
        current = self.head
        count = 0
        # Loop until you get to a Node that has next item as None
        while current != None :
            # Increment the count
            count = count + 1
            # Get the next node
            current = current.getNext()

        return count

    def search (self, item):
        # Get the head node
        current = self.head
        found = False
        stop = False
        # Loop until you get to a Node that has next item as None
        # and the item has not been found
        # and the flag doesn't say to stop
        while current != None and not found and not stop:
            # See if the data of this item matches what we are looking for
            if current.getData() == item:
                found = True
            else:
                # if the current item is greater than what we
                # are looking for
                if current.getData() > item:
                    # No need to keep looking - STOP
                    stop = True
                else:
                    # Get the next node9
                    current = current.getNext()
        
        return found

    def remove (self, item):
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
        if previous == None:
            # Set the head to be the node after the current
            self.head = current.getNext()
        else:
            # Set the next for the previous to be the one after the
            # current node (the current is being removed from the list)
            previous.setNext(current.getNext())

    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()


if __name__=="__main__":
    listTest = OrderedList()
    print(listTest.isEmpty())
    listTest.add("Hi")
    listTest.add("There")
    listTest.add("All")
    # listTest.add(123456789)
    # listTest.add(str(123456789))
    print(listTest.length())
    print(listTest.search("Hi"))
    print(listTest.search("His"))
    listTest.printList()
    listTest.remove("There")
    print(listTest.length())
