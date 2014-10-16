######################################
# Lab 5: Deques & Doubly-Linked Lists
# Exercise 3
#
# 9/24/13
#
# palindrome.py
#######################################

from Deque import *


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.enque(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.deque()
        print("first", first)
        last = chardeque.pop()
        print("pop", last)
        if first != last:
            stillEqual = False
            break
    return stillEqual


if __name__ == "__main__":
    tests = {"monty": False,
            "radar": True,
            "racecar": True,
            "palindrome": False,
            "civic": True}

    for (word, truth) in tests.items():
        result = palchecker(word)
        #i know this is
        comparison = result == truth
        print(word + "\n\t" + "Correct results?: " + str(comparison))

