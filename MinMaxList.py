#########################
# Lab 9
# Author: Mathew Younan
# Email: younanm@my.yorku.ca
# Section B
# Student ID: 218709188
#########################

class MinMaxList:

    def __init__(self, initializeList):
        self.listData = initializeList
        self.listData.sort()

    def insertItem(self, item, printResult=False/True):
        location = 0
        item_list = [item]
        if(len(self.listData) == 0):
            self.listData.append(item)
            location = 0
        elif(item >= self.listData[-1]):
            self.listData.append(item)
            location = len(self.listData) - 1
        elif(item <= self.listData[0]):
            self.listData = item_list + self.listData[0:]
            location = 0
        else:
            for i in range(len(self.listData)):
                if(item <= self.listData[i]):
                    end_section = self.listData[i:]
                    start_section = self.listData[0:i]
                    self.listData = start_section + item_list + end_section
                    location = i
                    break
        if (printResult):
            print("Item", item, "inserted at location", location)
            self.printList()

    # def getMinMax(self, minormax):
    #     if len(self.listData) == 0:
    #         return None
    #     if minormax == "MAX":
    #         result = self.listData[-1]
    #         del self.listData[-1]
    #     else:
    #         result = self.listData[0]
    #         del self.listData[0]
    #
    #     return result

    def getMin(self):
        result = self.listData[0]
        del self.listData[0]

        return result

    def getMax(self):
        result = self.listData[-1]
        del self.listData[-1]

        return result

    def printList(self):
        print(self.listData)


# Main function is given.
def main():
    aList = MinMaxList([10, 11, 99, 1, 34, 88])
    bList = MinMaxList([88, 0])
    print("Starting aList: ", aList.listData)
    print("Starting bList: ", bList.listData)

    aList.printList()
    bList.printList()

    aList.insertItem(97)
    bList.insertItem(3)
    print("Insert 97 to aList")
    print("Instert 3 to bList")

    aList.printList()
    bList.printList()

if __name__ == "__main__":
    main()