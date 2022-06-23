#########################
# Lab 7
# Author: Mathew Younan
# Email: younanm@my.yorku.ca
# Section B
# Student ID: 218709188
#########################

import pytest # Importing of the pytest library
from typing import List # From the typing library, import the List object

# Accepts a list of integers
def initializeMinMaxList(myList: List[int]) -> None:   # given
    myList.sort()

def insertItem(myList: List[int], item: int) -> None:  # given
    myList.append(item)
    myList.sort()

def getMinMax(myList: List[int], minormax: str) -> int:   # given -- but requires additional assert
    assert minormax.upper()=="MAX" or minormax.upper()=="MIN", "2nd argument must be 'Min' or 'Max' "
    assert len(myList) > 0, "List must not be empty." # Asserts that the length of myList is greater than 0 (checks if empty). If it is, output assertion message
    result: int
    if minormax == "MAX": # If max
        result = myList[-1] # Take the largest value (at the end of the sorted list)
        del myList[-1] # Delete this index from the list
    else: # if min
        result = myList[0] # Take the smallest value (at the front of the sorted list)
        del myList[0] # Delete this index from the list
    return result # Return the result back to the calling function

# Main function is given.
def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88] # aList, contains static integers as such
    print("Starting List: ", aList) # Output the starting list
    initializeMinMaxList(aList) # Sort the list
    min1 = getMinMax(aList, "MIN") # Call getMinMax function, looking for a minimum number, store that number under min1
    print("1st min: %d" % (min1)) # Output this number to the user
    min2 = getMinMax(aList, "MIN") # Call getMinMax function, looking for a minimum number, store that number under min2
    print("2nd min: %d" % (min2)) # Output this number to the user
    max1 = getMinMax(aList, "MAX") # Call getMinMax function, looking for a maximum number, store that number under max1
    print("1st max: %d" % (max1)) # Output this number to the user
    max2 = getMinMax(aList, "MAX") # Call getMinMax function, looking for a maximum number, store that number under max2
    print("2nd max: %d" % (max2)) # Output this number to the user

    # Inserting different integers into our list
    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)

    # Perform getMinMax 2 times to find min numbers, then 2 more times to find 2 max numbers again
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("DONE.  Type Enter to exit.")
    input()



if __name__ == "__main__":
    main()


#####
# WRITE YOUR TEST CASES BELOW HERE
#
######

def test_getMinMaxCase1(): # pytest edge case 1
    sample_list = [18, 7] # List with 2 elements
    initializeMinMaxList(sample_list) # Sort the list
    x = getMinMax(sample_list, "MIN") # Extract minimum number from list, set x equal to the result of function
    assert x < sample_list[0], "Min should be x" # Assert that x is less than the first index of the list, otherwise throw AssertionError
    y = getMinMax(sample_list, "MAX") # Extract maximum number from list, set y equal to the result of function
    assert y > x, "Max should be y" # Assert that y is greater than x, otherwise throw AssertionError

def test_getMinMaxCase2(): # pytest edge case 2
    sample_list = [15] # List with one element
    temp = sample_list[0] # Set temporary variable equal to the only element in the list
    initializeMinMaxList(sample_list) # Sort list (does nothing since there is only one element)
    y = getMinMax(sample_list, "MIN") # Extract minimum number from list, set y equal to the result of function
    assert y == temp, "Min should be y" # Assert that y is equal to temp, otherwise throw AssertionError
    insertItem(sample_list, y) # Insert y back into the list
    y = getMinMax(sample_list, "MAX") # Reassign y to the result of the maximum number in the list by calling getMinMax function
    assert y == temp, "Max should be y" # Assert that y is equal to temp, otherwise throw AssertionError

def test_getMinMaxCase3(): # pytest edge case 3
    sample_list = [] # Create empty list
    initializeMinMaxList(sample_list) # Call initializeMinMaxList function, passing in the empty list
    x = 4 # Set x equal to the lower number which we will push into the list
    y = 11 # Set y equal to the higher number which we will push into the list
    insertItem(sample_list, x) # Insert x into our list
    insertItem(sample_list, y) # Insert y into our list
    minimum = getMinMax(sample_list, "MIN") # Extract minimum number from list, set minimum equal to the result of function
    assert minimum == x, "Min should be x" # Assert that minimum is equal to x, otherwise throw AssertionError
    maximum = getMinMax(sample_list, "MAX") # Extract maximum number from list, set maximum equal to the result of function
    assert maximum == y, "Max should be y" # Assert that maximum is equal to y, otherwise throw AssertionError

def test_getMinMaxRequestError(): # Function which will test our getMinMax function to see if it handles incorrect string argument
    sample_list = [16, 4, 9] # Declare list with 3 elements
    initializeMinMaxList(sample_list) # Call initializeMinMaxList function, passing in our list of 3 elements
    with pytest.raises(AssertionError) as e: # Have e store the result of the block within
        temp = getMinMax(sample_list, "MID") # Execute this line, attempting to pass in "MID" as a parameter
    assert e.typename == "AssertionError", "Should raise AssertionError!" # Assert that e was an assertion error, otherwise throw an AssertionError message saying "Should raise AssertionError!"

def test_getMinMaxEmptyError(): # Function which will test our getMinMax function to see if it handles an empty list properly
    sample_list = [] # Declaration of empty list
    initializeMinMaxList(sample_list) # Call initializeMinMaxList function, passing in our empty list
    with pytest.raises(AssertionError) as e: # Have e store the result of the block within
        temp = getMinMax(sample_list, "MIN") # Execute this line, attempting to call getMinMax function on empty list
    assert e.typename == "AssertionError", "Should raise AssertionError!" # Assert that e was an assertion error, otherwise throw an AssertionError message saying "Should raise AssertionError!"