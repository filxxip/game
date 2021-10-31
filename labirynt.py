board_index = []
import random
from datetime import datetime
from getkey import getkey, keys
import copy
import time
import os
from threading import Thread

from colorama import init, Fore, Back, Style
def cleaar():
    os.system('cls' if os.name == 'nt' else 'clear')
def board_create():
    for x in range(0, 40):
        board_index.append([])
    for x in range(0, 40):
        for y in range(0, 65):
            board_index[x].append(" ")
    for x in range(1, 40):
        board_index[x][0] = "|"
        board_index[x][64] = "|"
    for x in range(1, 64):
        board_index[0][x] = "_"
        board_index[39][x] = "_"
    board_index[random.randrange(1, 39)][random.randrange(1, 64)] = "x"
    for x in range (0, 1200):
        number1 = random.randrange(1, 39)
        number2 = random.randrange(1, 64)
        while board_index[number1][number2] != " ":
            number1 = random.randrange(1, 39)
            number2 = random.randrange(1, 64)
        board_index[number1][number2] = "#"
    for x in range(1, 39):
        for y in range(1, 64):
            help = []
            help.append(board_index[x-1][y])
            help.append(board_index[x+1][y])
            help.append(board_index[x][y+1])
            help.append(board_index[x][y-1])
            if help.count("#") == 4 :
                number3 = random.sample([0, 1, 2, 3], 2)
                if 0 in number3 : board_index[x-1][y] = " "
                if 1 in number3 : board_index[x+1][y] = " "
                if 2 in number3 : board_index[x][y-1] = " "
                if 3 in number3 : board_index[x][y+1] = " "
            elif help.count("#") == 3:
                number3 = random.choice([0, 1, 2])
                if number3 == 0:
                    if board_index[x-1][y]=="#": board_index[x-1][y] = " "
                    else: board_index[x+1][y] = " "
                elif number3 == 1:
                    if board_index[x+1][y]=="#": board_index[x+1][y] = " "
                    else: board_index[x][y+1] = " "
                elif number3 == 2:
                    if board_index[x][y+1]=="#": board_index[x][y+1] = " "
                    else: board_index[x][y-1] = " "
    for x in range (0, 10):
        number1 = random.randrange(1, 39)
        number2 = random.randrange(1, 64)
        while board_index[number1][number2] in( "#", "x", "T", "M"):
            number1 = random.randrange(1, 39)
            number2 = random.randrange(1, 64)
        board_index[number1][number2] = "$"
    for x in range (0, 7):
        number1 = random.randrange(1, 39)
        number2 = random.randrange(1, 64)
        while board_index[number1][number2] in( "#", "x", "$", "M"):
            number1 = random.randrange(1, 39)
            number2 = random.randrange(1, 64)
        board_index[number1][number2] = "t"
    number1 = random.randrange(1, 36)
    number2 = random.randrange(1, 61)
    while (board_index[number1][number2] or board_index[number1][number2+1] or board_index[number1][number2+2] or board_index[number1][number2+3]) in( "x", "$", "T"):
        number1 = random.randrange(1, 36)
        number2 = random.randrange(1, 61)
    board_index[number1][number2] = "M"
    board_index[number1][number2+1] = "E"
    board_index[number1][number2+2] = "T"
    board_index[number1][number2+3] = "A"
    
def game_rules():

    cleaar()
    print("""
    LABIRINTH
    Your task is to get in 300 seconds to the META subtitle.
    If you win, you will get 3000 money!!
    Collect every "$" to get extra coins.
    Collection of "T" will get you extra time.
    Good luck!
    
    click ENTER if you read it...""")
    enter = input("")

def get_board():
    for x in range(0, 40):
        for y in range(0, 65):
            if board_index[x][y] == "#" : print("\033[38;5;241m"+board_index[x][y], end ="")
            elif board_index[x][y] == "$" : print("\033[38;5;226m"+board_index[x][y], end ="")
            elif board_index[x][y] == "t"  : print("\033[38;5;40m"+board_index[x][y], end ="")
            else: print("\033[38;5;21m"+board_index[x][y], end ="")
        print("")
    print("\033[38;5;255m")
    
def b_m():
    global key
    key = None
    click2 = True
    while click2 :
        key = getkey()
        time.sleep(0.08)
        if key == "q":
            quit()
        global click
        if click == False : click2 = False
        
def board_move(index):
    board_index2 = copy.deepcopy(board_index)
    for x in range(1, 39): 
        for y in range(1, 64):
            if board_index2[x][y] == "x": 
                board_index2[x][y] = " "
                coordinates = [x, y]
    start = datetime.now()
    time1 = start.hour*60*60 + start.minute*60 + start.second + start.microsecond/1000000
    printer = printer2 = 30
    win = 0
    global click
    click = True
    time.sleep(3)
    while click:
        cleaar()
        get_board()
        now = datetime.now()
        time2 = now.hour*60*60 + now.minute*60 + now.second + now.microsecond/1000000
        print("Game time:",  round(120 - (time2-time1), 1))
        print("Earned money:",win)
        if printer <30:
            print("You get ", time_plus, "seconds!!")
            printer +=1
        if printer2 < 30:
            print("You get ",money_plus, "coins!!")
            printer2 +=1
        time.sleep(0.08)
        global key
        if key == "w":
            coordinates[0]-=1
            if 39>coordinates[0] >0 and 64>coordinates[1] >0 and board_index[coordinates[0]][coordinates[1]] not in ("#"):
                board_index[coordinates[0]][coordinates[1]] = "x"
                board_index[coordinates[0]+1][coordinates[1]] = board_index2[coordinates[0]+1][coordinates[1]]
            else: coordinates[0]+=1
        elif key == "s":
            coordinates[0]+=1
            if 39>coordinates[0] >0 and 64>coordinates[1] >0 and board_index[coordinates[0]][coordinates[1]] not in ("#"):
                board_index[coordinates[0]][coordinates[1]] = "x"
                board_index[coordinates[0]-1][coordinates[1]] = board_index2[coordinates[0]-1][coordinates[1]]
            else: coordinates[0]-=1
        elif key == "a":
            coordinates[1]-=1
            if 39>coordinates[0] >0 and 64>coordinates[1] >0 and board_index[coordinates[0]][coordinates[1]] not in ("#"):
                board_index[coordinates[0]][coordinates[1]] = "x"
                board_index[coordinates[0]][coordinates[1]+1] =  board_index2[coordinates[0]][coordinates[1]+1]
            else: coordinates[1]+=1
        elif key == "d":
            coordinates[1]+=1
            if 39>coordinates[0] >0 and 64>coordinates[1] >0 and board_index[coordinates[0]][coordinates[1]] not in ("#"):
                board_index[coordinates[0]][coordinates[1]] = "x"
                board_index[coordinates[0]][coordinates[1]-1] = board_index2[coordinates[0]][coordinates[1]-1]
            else: coordinates[1]-=1
        elif key == "q":
            exit()
        if board_index2[coordinates[0]][coordinates[1]] ==  "$":
            money_plus = money_getter()
            win += money_plus
            printer2 = 0
            board_index2[coordinates[0]][coordinates[1]] = " "
        elif board_index2[coordinates[0]][coordinates[1]] == "t":
            time_plus = time_getter()
            time1 = time1 + time_plus
            board_index2[coordinates[0]][coordinates[1]] = " "
            printer = 0
        elif (board_index2[coordinates[0]][coordinates[1]] or board_index2[coordinates[0]][coordinates[1]] or board_index2[coordinates[0]][coordinates[1]] or board_index2[coordinates[0]][coordinates[1]]) in ("M", "E", "T", "A"):
            click = False
            print("Congratulation!!!!")
            win += 3000
            print("Your win: ", win)
            from mainprogram import users, User
            users[index].set_money(users[index].get_money() + win)
            print("click ENTER to end your game..")
        if round(120 - (time2-time1), 1)<=0:
            print("Game over ;/")
            print("click ENTER to end your game..")
            click = False
        key = None
def money_getter():
    number = random.randrange(0, 1001)
    return number
def time_getter():
    rantime = random.randrange(0, 50)
    return rantime

def main_labirynt(index):
    board_create()
    game_rules()
    if __name__ == 'labirynt':
        Thread(target = b_m).start()
        Thread(target = board_move(index)).start()
        
