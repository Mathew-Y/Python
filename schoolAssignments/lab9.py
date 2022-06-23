#########################
# Lab 9
# Author: Mathew Younan
# Email: younanm@my.yorku.ca
# Section B
# Student ID: 218709188
#########################

from MinMaxList import MinMaxList
from random import randint

def main():
    aList = MinMaxList([10, 11, 99, 1, 34, 88])
    print("--Insert Item--")
    for i in range(30):
        x = randint(1, 100)
        aList.insertItem(x, True) # You need to modify insertItem (See Task 2)

    print("--Get Min--")
    for i in range(10):
        print("Min item %d " % aList.getMin() ) # Notice that the getMinMax() method has been changed.
        aList.printList() # printList() is a new method

    print("--Get Max--")
    for i in range(10):
        print("Max item %d " % aList.getMax() ) # Notice that the getMinMax() method has been replaced.
        aList.printList() # printList() is a new method

if __name__ == "__main__":
 main()