board_index = []
import random
from datetime import datetime
from getkey import getkey, keys
import copy
import time
import os
from threading import Thread
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
        while board_index[number1][number2] in( "#", "x", "T"):
            number1 = random.randrange(1, 39)
            number2 = random.randrange(1, 64)
        board_index[number1][number2] = "$"
    for x in range (0, 7):
        number1 = random.randrange(1, 39)
        number2 = random.randrange(1, 64)
        while board_index[number1][number2] in( "#", "x", "$"):
            number1 = random.randrange(1, 39)
            number2 = random.randrange(1, 64)
        board_index[number1][number2] = "T"
    start = datetime.now()
    global time1
    time1 = start.hour*60*60 + start.minute*60 + start.second + start.microsecond/1000000
    


def get_board():
    for x in range(0, 40):
        for y in range(0, 65):
            print(board_index[x][y], end ="")
        print("")
    
def b_m():
    global key
    key = None
    while True:
        key = getkey()
        time.sleep(0.08)
        if key == "q":
            quit()


def board_move():
    board_index2 = copy.deepcopy(board_index)
    for x in range(1, 39): 
        for y in range(1, 64):
            if board_index2[x][y] == "x": 
                board_index2[x][y] = " "
                coordinates = [x, y]
    click = True
    while click:
        cleaar()
        get_board()
        now = datetime.now()
        time2 = now.hour*60*60 + now.minute*60 + now.second + now.microsecond/1000000
        print("Game time:",  300 - round(time2-time1, 1))
        
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
        if board_index2[coordinates[0]][coordinates[1]] in ("$", "T"):
            board_index2[coordinates[0]][coordinates[1]] = " "
        
        key = None

def money_getter():
    number = random.randrange(0, 1001)
    #users[index].set_money(users[index].get_money()+number)
board_create()
if __name__ == '__main__':
    Thread(target = board_move).start()
    Thread(target = b_m).start()