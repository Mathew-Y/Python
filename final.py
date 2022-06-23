###########################################
# EECS1015 - Final exam (final.py)
# Name: Mathew Younan
# Student ID: 218709188
# Email: younanm@my.yorku.ca
# Section B
###########################################

# import the approriate items from utilities.py and other modules may you require
import random
import time
from utilities import students
from utilities import studentsInfo
from utilities import SeaLife

def task0():
    print("Final Exam - EECS1015")
    print("Name: Mathew Younan")
    print("Student ID: 218709188")
    print("email: younanm@my.yorku.ca")
    print("Section B")

def printOutcome(userSelection, computerSelection):
    if userSelection == computerSelection:
        print("A tie!")
        return
    elif (userSelection == 1 and computerSelection == 3) or (userSelection == 2 and computerSelection == 1) or (userSelection == 3 and computerSelection == 2):
        print("You win!")
    else:
        print("HAL wins!")

def task1():
    choice_mapping = {1: "rock", 2: "paper", 3: "scissors"}
    while True:
        choice_string = ""
        computer_choice = random.randint(1, 3)
        computer_string = ""
        print("Rock, Paper, Scissors!")
        print("Make your selection. . .")
        while True:
            user_choice = int(input("(1) rock, (2) paper, (3) scissors?: "))

            if user_choice != 1 and user_choice != 2 and user_choice != 3:
                print("Invalid selection. Try again.")
            else:
                break

        choice_string = choice_mapping[user_choice]
        computer_string = choice_mapping[computer_choice]

        print("You:", choice_string)
        print("HAL:", computer_string)

        printOutcome(user_choice, computer_choice)

        play_again_response = input("Play again (Y/N)?: ")

        if play_again_response.lower() != "y":
            break

def swapAdjacentElements(alist):
    counter = 0

    for i in range(len(alist)//2):
        temp = alist[counter]
        alist[counter] = alist[counter + 1]
        alist[counter + 1] = temp
        counter += 2

def task2():
    user_string = input("Input two or more chars separated by spaces: ")
    user_string = user_string.replace(" ", "")
    assert len(user_string) >= 2, "Must enter two or more characters!"

    list_version = list(user_string)
    print("Initial list")
    print(list_version)
    swapAdjacentElements(list_version)
    print("Modified list")
    print(list_version)
    str_version = ''.join(list_version)
    print("String version: '" + str_version + "'")

def task3():
    individual_info = {}
    student_year = ""
    student_degree = ""
    student_living = ""
    for i in range(len(students)):
        if(i in studentsInfo.get("Year 1")):
            student_year = "Year 1"
        elif(i in studentsInfo.get("Year 2")):
            student_year = "Year 2"
        elif (i in studentsInfo.get("Year 3")):
            student_year = "Year 3"
        else:
            student_year = "Year 4"

        if(i in studentsInfo.get("CS")):
            student_degree = "CS"
        elif(i in studentsInfo.get("DM")):
            student_degree = "DM"
        elif (i in studentsInfo.get("BZ")):
            student_degree = "BZ"
        else:
            student_degree = "SE"

        if(i in studentsInfo.get("On Campus")):
            student_living = "On Campus"
        else:
            student_living = "Off Campus"

        dic_value = [student_year, student_degree, student_living]
        individual_info[students[i]] = dic_value

    sorted_dict = {key: value for key, value in sorted(individual_info.items())}

    for key in sorted_dict:
        print(" " * (10 - len(key)) + key + " (" + sorted_dict.get(key)[0] + ") Program: " + sorted_dict.get(key)[1] + " Housing: " + sorted_dict.get(key)[2])

def task4():
    creature_list = []
    input("Press enter to start the aquarium.")

    for i in range(5):
        pos = random.randint(5, 30)
        direction = random.randint(0, 1)
        creature = SeaLife(direction, pos)
        creature_list.append(creature)

    time_step = 1

    for i in range(50):
        print(40 * "-" + "Time:", time_step)

        for creature in creature_list:
            print(creature.getStr())
            creature.move()

        time.sleep(0.3)
        time_step += 1

def main():
    print("\n--------- Task0: Submission Info       ------------")
    task0()
    print("\n--------- Task1: Rock, Paper, Scissors ------------")
    task1()
    print("\n--------- Task2: Swap List Elements    ------------")
    task2()
    print("\n--------- Task3: Student Info          ------------")
    task3()
    print("\n--------- Task4: Aquarium              ------------")
    task4()

    input("Press enter to quit.")


if __name__ == "__main__":
    main()