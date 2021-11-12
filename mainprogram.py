from datetime import datetime
from getkey import getkey, keys
import random
import os
import time
import re
import copy
from game_1 import gra
from game_2 import gra2
from threading import Thread
from labirynt import main_labirynt
from bank import bankk
from ball import balll
def cleaar():
    os.system('cls' if os.name == 'nt' else 'clear')
class Energy(object):
    def __init__(self, number):
        self.__number = number
        self.set_name()
    def set_name(self):
        self.__name = str(self.__number)+" energy"
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number


class User(object):
    def __init__(self, name, money=1000, energy=100, create_date=datetime.now(), inventory = []):
        self.__name = name
        self.__money = float(money)
        self.__energy = float(energy)
        self.__create_date = create_date
        self.__inventory = inventory

    def set_money(self, money):
        if money >= 0:
            self.__money = money
        if money <=0:
            self.__money = 0
    def add_inventory(self, item):
        self.__inventory.append(item)
    def del_inventory(self, index):
        del self.__inventory[index]


    def set_energy(self, energy):
        if energy >= 0:
            self.__energy = energy
        if energy > 100:
            self.__energy = 100
        if energy <0:
            self.__energy = 0
    def get_inventory(self):
        return self.__inventory
    def get_name(self):
        return self.__name

    def get_money(self):
        return self.__money

    def get_energy(self):
        return self.__energy

    def get_level(self):
        days1 = (
            datetime.now().year * 365 * 30
            + datetime.now().month * 30
            + datetime.now().day
        )
        days2 = (
            self.__create_date.year * 365 * 30
            + self.__create_date.month * 30
            + self.__create_date.day
        )
        exist_time = days1 - days2
        self.__level = "Amatour"
        if exist_time > 10:
            self.__level = "Begginer"
        if exist_time > 30:
            self.__level = "Novice"
        if exist_time > 50:
            self.__level = "Proffesional"
        if exist_time > 100:
            self.__level = "World Class"
        if exist_time > 300:
            self.__level = "Legendary"
        if exist_time > 500:
            self.__level = "Ultimate"
        return self.__level
    def get_create_date(self):
        return self.__create_date

    def get_exist_time(self):
        self.__exist_time = datetime.now() - self.__create_date
        return self.__exist_time
users = []
board_index = []
def user_create():
    cleaar()
    user_file = open("user_database.txt", "a")
    user_file_2 = open("user_database_2.txt", "a")
    bank_dep = open("user_bank_deposit.txt", "a")
    bank_cred = open("user_bank_credit.txt", "a")
    bank_cred.write("#;\n")
    bank_dep.write("#;\n")
    bank_dep.close()
    bank_cred.close()
    name = input("Write your name: ")
    print("User created")
    users.append(User(name))
    time.sleep(2)
    index = len(users)-1
    user_info = (name, ",",  str(users[index].get_money()), ",", str(users[index].get_energy()), ",", str(users[index].get_create_date()), "\n")
    user_file.writelines(user_info)
    if len(users[index].get_inventory()) > 0:
        for x in users[index].get_inventory(): user_file_2.writelines((x, ","))
    user_file_2.write("\n")
    user_file_2.close()

    user_file.close()

def create_from_file():
    user_file_2 = open("user_database_2.txt", "r")
    user_file = open("user_database.txt", "r")
    for line in user_file:
        info2 = []
        info = re.split("\,+", user_file_2.readline().rstrip())
        print(info)
        for x in info:
            if x == "":
                info.remove(x)
            else:
                info2.append(Energy(int(x)))
        information = re.split("[\ \:\,\-]", line)
        information[-1] = information[-1].rstrip()
        help = re.split("\.", information[8])
        users.append(User(information[0], float(information[1]), float(information[2]), 
        datetime(int(information[3]), int(information[4]), int(information[5]),
        int(information[6]), int(information[7]), int(help[0]), int(help[1])), inventory = info2))
    user_file.close()
    user_file_2.close()

def update_file():
    user_file = open("user_database.txt", "w")
    user_file_2 = open("user_database_2.txt", "w")
    for index in range(0, len(users)):
        user_info = (users[index].get_name(), ",",  str(users[index].get_money()), ",", 
        str(users[index].get_energy()), ",", str(users[index].get_create_date()), "\n")
        user_file.writelines(user_info)
        for x in users[index].get_inventory():
            user_file_2.writelines((str(x.get_number()), ","))
        user_file_2.write("\n")
    user_file.close()
    user_file_2.close()

def board_create():
    for x in range(0, 30):
        board_index.append([])
    for x in range(0, 30):
        for y in range(0, 55):
            board_index[x].append(" ")
    for x in range(1, 30):
        board_index[x][0] = "|"
        board_index[x][54] = "|"
    for x in range(1, 54):
        board_index[0][x] = "_"
        board_index[29][x] = "_"
    board_index[28][1] = "x"

        

def get_board(index):
    for x in range(0, 30):
        for y in range(0, 55):
            print(board_index[x][y], end ="")
        print("")
    print("\n\n\nName:", users[index].get_name())
    print("Money:", users[index].get_money())
    print("Energy:", users[index].get_energy())
    print("Created date:", users[index].get_create_date())
    print("Level:", users[index].get_level())
    print("Exist time:", users[index].get_exist_time())
    print("\n\n1 - shop")
    print("2 - get energy")
    print("3 - INVENTORY-user")

def shop(index):
    cleaar()
    print("""
    1 - 20'%' energy - 20$
    2 - 40'%' energy - 30$
    3 - 50'%' energy - 35$
    4 - 100'%' energy - 50$
    0 - return
    """)
    opt = input("Which option do you choose? ")
    if opt =="0":
        get_board(index)
    elif opt == "1":
        if users[index].get_money() >=20:
            users[index].set_money(users[index].get_money()-20)
            users[index].set_energy(users[index].get_energy()+20)
    elif opt == "2":
        if users[index].get_money() >=30:
            users[index].set_money(users[index].get_money()-30)
            users[index].set_energy(users[index].get_energy()+40)
    elif opt == "3":
        if users[index].get_money() >=35:
            users[index].set_money(users[index].get_money()-35)
            users[index].set_energy(users[index].get_energy()+50)
    elif opt == "4":
        if users[index].get_money() >=50:
            users[index].set_money(users[index].get_money()-50)
            users[index].set_energy(users[index].get_energy()+100)
    else:
        print("Incorrect choice..")
        time.sleep(1)
        shop(index)
    get_board(index)
        
def energy_getter(index):
    cleaar()
    diffrent = 100 - users[index].get_energy()
    t = diffrent*0.1
    while users[index].get_energy() < 100:
        energy = int(users[index].get_energy()//10)
        print("{" + ("|"*energy) + ("-"*(10-energy)) + "}")
        time.sleep(0.02)
        users[index].set_energy(users[index].get_energy()+1)
        cleaar()

def board_move(index):
    for x in range(0, 5):
        first = int(random.randrange(1, 29))
        second = int(random.randrange(1, 54))
        while board_index[first][second] != " ":
            first = int(random.randrange(1, 29))
            second = int(random.randrange(1, 54))
        board_index[first][second] = "*"
    for x in range(0, 6):
        first = int(random.randrange(1, 29))
        second = int(random.randrange(1, 54))
        while board_index[first][second] != " ":
            first = int(random.randrange(1, 29))
            second = int(random.randrange(1, 54))
        board_index[first][second] = "#"
    first = int(random.randrange(1, 26))
    second = int(random.randrange(1, 51))
    while board_index[first][second] != " ":
        first = int(random.randrange(1, 26))
        second = int(random.randrange(1, 51))
    board_index[first][second] = "B"
    board_index[first][second+1] = "A"
    board_index[first][second+2] = "N"
    board_index[first][second+3] = "K"
    board_index2 = copy.deepcopy(board_index)
    coordinates = [28, 1]
    board_index2[coordinates[0]][coordinates[1]] = " "
    click = True
    key = None
    while click:
        cleaar()
        get_board(index)
        if key in ("w", "a", "s", "d"):
            mystery(coordinates, index, board_index2)
            condition = True
            while condition:
                game_funtion(coordinates, index, board_index2)
                condition = False
            bank(coordinates, index, board_index2)
        time.sleep(0.000002)
        key = getkey()
        if key == "0":
            menu_2()
        elif key == "q":
            fun_exit()
        elif key == "1":
            shop(index)
        elif key == "2":
            energy_getter(index)
        elif key == "3":
            inventory_user(index)
        if users[index].get_energy() > 0:
            if key == "w":
                coordinates[0]-=1
                if 29>coordinates[0] >0 and 54>coordinates[1] >0:
                    board_index[coordinates[0]][coordinates[1]] = "x"
                    board_index[coordinates[0]+1][coordinates[1]] = board_index2[coordinates[0]+1][coordinates[1]]
                else: coordinates[0]+=1
            elif key == "s":
                coordinates[0]+=1
                if 29>coordinates[0] >0 and 54>coordinates[1] >0:
                    board_index[coordinates[0]][coordinates[1]] = "x"
                    board_index[coordinates[0]-1][coordinates[1]] = board_index2[coordinates[0]-1][coordinates[1]]
                else: coordinates[0]-=1
            elif key == "a":
                coordinates[1]-=1
                if 29>coordinates[0] >0 and 54>coordinates[1] >0:
                    board_index[coordinates[0]][coordinates[1]] = "x"
                    board_index[coordinates[0]][coordinates[1]+1] =  board_index2[coordinates[0]][coordinates[1]+1]
                else: coordinates[1]+=1
            elif key == "d":
                coordinates[1]+=1
                if 29>coordinates[0] >0 and 54>coordinates[1] >0:
                    board_index[coordinates[0]][coordinates[1]] = "x"
                    board_index[coordinates[0]][coordinates[1]-1] = board_index2[coordinates[0]][coordinates[1]-1]
                else: coordinates[1]-=1
            if key in("w", "s", "a", "d"):
                energy = users[index].get_energy() - 1
                users[index].set_energy(energy)

def inventory_user(index):
    cleaar()
    print("INVENTORY: ")
    for x in range(0, len(users[index].get_inventory())):
        print(x+1," - ", users[index].get_inventory()[x].get_name())
    choose = input("\n\nWhich one you want to use, write relevant number\nIf you want to return click 0 :" )
    try:
        users[index].set_energy(users[index].get_energy()+users[index].get_inventory()[int(choose)-1].get_number())
        users[index].del_inventory(int(choose)-1)
    except IndexError : pass
    except ValueError : pass

def bank(coordinates, index, board_index2):
    if board_index2[coordinates[0]][coordinates[1]] in ("B", "A", "N", "K"):
        cleaar()
        bankk(index)
def mystery(coordinates, index, board_index2):
    if board_index2[coordinates[0]][coordinates[1]] == "#":
        time.sleep(1)
        cleaar()
        suprise = random.choice(("money", "energy", "potions"))
        if suprise == "money":
            num2 = random.randrange(-1000, 1001)
            users[index].set_money(users[index].get_money()+num2)
            if num2 >=0: print("YEAH, you've won", num2, "money")
            elif num2<0: print("Unfortunetelly, you've lost", num2, "money")
        if suprise == "energy":
            num2 = random.randrange(-100, 101)
            users[index].set_energy(users[index].get_energy()+num2)
            if num2 >=0: print("YEAH, you've won", num2, "energy")
            elif num2<0: print("Unfortunetelly, you've lost", num2, "energy")
        if suprise == "potions":
            num2 = random.choice((Energy(10), Energy(20), Energy(30), Energy(40), Energy(50), Energy(60), Energy(70)))
            print("YEAH, you've won", num2.get_number(), "energy for later")
            users[index].add_inventory(num2)
        time.sleep(1)
        cleaar()
        get_board(index)

def game_funtion(coordinates, index, board_index2):
    if board_index2[coordinates[0]][coordinates[1]] == "*":
        time.sleep(1)
        cleaar()
        game = random.choice(("game_1", "game_2", "labirynt", "ball"))
        if game == "game_1":
            gra(index)
        elif game == "game_2":
            gra2(index)
        elif game == "labirynt":
            main_labirynt(index)
        elif game == "ball":

            balll(index)
        time.sleep(1)
        cleaar()
        get_board(index)


def get_list_users():
    cleaar()
    num =1
    for x in range(0, len(users)):
        print(num, " - ", users[num-1].get_name())
        num +=1
def fun_exit():
    update_file()
    exit()
def menu_2():
    global index
    get_list_users()
    try:
        index = input("Select relevant person(if you want to return, click '0'): ")
        if index =="q" : fun_exit()
        if index == "0" : menu_1()
        index = int(index)-1
        while index not in range(0, len(users)):
            index = int(input("Select relevant person: "))-1
    except ValueError: 
        print("Incorrect value")
        menu_2()

def menu_1():
    cleaar()
    print("""
    1 - create new user
    2 - delete an user
    3 - login to your account
    q - exit
    """)
    choose = input("")
    if choose == "1":
        user_create()
        menu_1()
    elif choose == "2":
        get_list_users()
        delete = input("Which one you want to delete? ")
        del users[int(delete)-1]
        menu_1()
    elif choose =="3":
        menu_2()
    elif choose == "q":
        update_file()
        fun_exit()
    else:
        cleaar()
        print("Try again..")
        time.sleep(1)
        menu_1()
def basic():
    create_from_file()
    board_create()
def main():
    cleaar()
    basic()
    menu_1()
    board_move(index)


