__author__ = 'newScanTron'
from DLL import*
dll = DLL()


class Deque:

    def __init__(self):
        var = None

    def addFront(self, item):
        dll.add(item)

    def enque(self, item):
        dll.append(item)

    def deque(self):
        return dll.removeHead()

    def pop(self):
        return dll.removeTail()

    def size(self):
        return dll.length()