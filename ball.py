import time
import os
from threading import Thread
from getkey import getkey, keys
import random
from colorama import init, Fore, Back, Style
board_index = []
def cleaar(): os.system('cls' if os.name == 'nt' else 'clear')
def board():
    for x in range(30):
        board_index.append([])
    for x in range(29):
        for y in range(40):
            if y==0:
                board_index[x].append("|")
            elif y==39:
                board_index[x].append("|\n")
            else:board_index[x].append(" ")
    board_index[29].append("|")
    for z in range(38):
        board_index[29].append("_")
    board_index[29].append("|\n")
    


class Ball(object):
    def __init__(self):
        self.__xcoo = random.randrange(1, 39)
        self.__ycoo = 0
    def get_x(self):
        return self.__xcoo
    def get_y(self):
        return self.__ycoo
    def change_y_coo(self):
        self.__ycoo+=1
class Coin(object):
    def __init__(self):
        self.__xcoo = random.randrange(1, 39)
        self.__ycoo = 0
    def get_x(self):
        return self.__xcoo
    def get_y(self):
        return self.__ycoo
    def change_y_coo(self):
        self.__ycoo+=1
class Life(object):
    def __init__(self):
        self.__xcoo = random.randrange(1, 39)
        self.__ycoo = 0
    def get_x(self):
        return self.__xcoo
    def get_y(self):
        return self.__ycoo
    def change_y_coo(self):
        self.__ycoo+=1
def get_board(index):
    points = 0
    coins = 0
    balls=[]
    balls.append(Ball())
    life = 3
    global stoppp
    while stoppp=="True":
        if balls[len(balls)-1].get_y()>5:balls.append(random.choice([Ball(), Coin(), Life()]))
        time.sleep(0.5)
        cleaar()
        for y in range(len(balls)):
            if balls[y].get_y() <28:
                balls[y].change_y_coo()
                board_index[balls[y].get_y()-1][balls[y].get_x()] = " "
                if type(balls[y]) is Ball:
                    board_index[balls[y].get_y()][balls[y].get_x()] = "O"
                if type(balls[y]) is Coin:
                    board_index[balls[y].get_y()][balls[y].get_x()] = "$"
                if type(balls[y]) is Life:
                    board_index[balls[y].get_y()][balls[y].get_x()] = "L"
            else:
                
                board_index[balls[y].get_y()][balls[y].get_x()] = " "
        for x in range(0, 30):
            for y in range(0, 40):
                if (x!=29) or (y!=39): 
                    if board_index[x][y] =="=":
                        print("\033[38;5;40m"+board_index[x][y], end ="")
                    else:
                        print("\033[38;5;255m"+board_index[x][y], end="")
                else:
                    print("\033[38;5;255m"+board_index[x][y])
        for x in range(1, 39):
            if board_index[28][x] in ("O", "$", "L") :
                if board_index[29][x] == "=":
                    points+=1
                    if board_index[28][x] =="$":
                        coins+= random.randrange(-10, 50)
                    if board_index[28][x] =="L":
                        life+= random.randrange(1, 4)
                else:
                    if board_index[28][x]=="O":
                        life-=1
        

        print("POINTS :", points)
        print("COINS :", coins)
        print("Life :", life)
        if life ==0:
            from mainprogram import users
            users[index].set_money(users[index].get_money()+(coins+20*points))
            print("Your win:", coins+20*points)
            print("click ENTER to end your game..") 
            stoppp = "False"
def my_object():
    yyy = 29
    xxx = 20
    key_ball = getkey()
    board_index[yyy][xxx-1] = "="
    board_index[yyy][xxx] = "="
    board_index[yyy][xxx+1] = "="
    global stoppp
    while stoppp=="True":
        key_ball = getkey()
        if key_ball == keys.RIGHT:
            if xxx <37:
                xxx+=1
                board_index[yyy][xxx-1] = "="
                board_index[yyy][xxx] = "="
                board_index[yyy][xxx+1] = "="
                board_index[yyy][xxx-2] = "_"
        elif key_ball == keys.LEFT:
            if xxx >2:
                xxx-=1
                board_index[yyy][xxx-1] = "="
                board_index[yyy][xxx] = "="
                board_index[yyy][xxx+1] = "="
                board_index[yyy][xxx+2] = "_"
def balll(index):

    board()
    global stoppp
    stoppp =  "True"
    if __name__ == 'ball':
        Thread(target = my_object).start()
        Thread(target = get_board, args=(index,)).start()
