#########################
# Lab 8
# Author: Mathew Younan
# Email: younanm@my.yorku.ca
# Section B
# Student ID: 218709188
#########################

import time
import random

class Snail:

    animations = ["__~@", "_~_@", "~__@"]

    def __init__(self, name: str):
        self.name = name.upper()
        assert len(name) == 2, "Snail's initials must be 2 characters."
        # self.speed = 0.9
        self.speed = random.randint(1, 10) / 10
        self.frame = 0
        self.pos = 0.0

    def move(self):
        self.pos += self.speed
        self.frame += 1
        if self.frame > 2:
            self.frame = 0

    def getIntPos(self):
        new_num = int(self.pos)
        return new_num

    def getName(self):
        return self.name

    def getStr(self):
        race_string = ""
        race_string = (" " * self.getIntPos()) + self.animations[self.frame] + (" " * (40 - self.getIntPos())) + self.name
        return race_string

def getSnailList():
    snails_list = []
    N = int(input("How many snails do you want to race?: "))
    for i in range(N):
        temp_name = input("What is the name of Snail #" + (str(i + 1)) + "?: ")
        temp_snail = Snail(temp_name)
        snails_list.append(temp_snail)
    return snails_list

def runRace(snail_list: list[Snail]):
    input("Please press enter to start the race.")
    time_step = 1
    plays_again = False
    check_won = "n"
    winners = []
    while(True):
        print(("-" * 40) + "Time  " + str(time_step))
        for snail in snail_list:
            print(snail.getStr())
            snail.move()
            if(snail.getIntPos() > 39):
                check_won = "y"
                winner = snail.name
                winners.append(snail.name)
            time.sleep(0.5)
        if check_won == "y":
            if(len(winners) > 1):
                win_message = "Winners: "
                for i in range(len(winners) - 1):
                    win_message += winners[i] + ", "
                win_message += "and " + winners[-1] + "!"
                print(win_message)
            else:
                print("Snail " + winner + " WON!")
            return
        time_step += 1

if __name__ == '__main__':
    while(True):
        print("Snail Race . . . .")
        snail_list = getSnailList()
        runRace(snail_list)
        response = input("Would you like to play again [y/n]?: ")

        if(response.lower() != "y"):
            print()
            break

