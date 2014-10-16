from node import *

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        # Check if the head is empty
        return self.head == None

    def add(self, item):
        # Create a node for the new item
        temp = Node(item)
        # Set the next item to be the current head
        temp.setNext(self.head)
        # Set the new head to be the new item
        self.head = temp

    def length (self):
        # Get the head node
        current = self.head
        count = 0
        # Loop until you get to a Node that has next item as None
        while current is not None :
            # Increment the count
            count = count + 1
            # Get the next node
            current = current.getNext()

        return count

    def search (self, item):
        # Get the head node
        current = self.head
        found = False
        # Loop until you get to a Node that has next item as None
        # and the item has not been found
        while current None and not found:
            # See if the data of this item matches what we are looking for
            if current.getData() == item:
                found = True
            else:
                # Get the next node
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
    listTest = UnorderedList()
    print(listTest.isEmpty())
    listTest.add("Hi")
    listTest.add("There")
    listTest.add("All")
    listTest.printList()
    print(listTest.length())
    print(listTest.search("Hi"))
    print(listTest.search("His"))
    listTest.remove("There")
    print(listTest.length())
