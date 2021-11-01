import re
from datetime import datetime
def deposit(index, a, users):
    user_bank_deposit = open("user_bank_deposit.txt", "r")
    deposits = user_bank_deposit.readlines()
    for x in range(0, len(deposits)):
        deposits[x] = deposits[x].rstrip()
    money = None
    while money == None:
        try: 
            money = int(input("How much money do want to put into the deposit? if you want to return click 0: "))
            #while money > users[index].get_money():
            print("You don't have enough money :(")
            money = int(input("How much money do want to put into the deposit? if you want to return, click 0: "))
            if money >0:
                rate = int(input("How many days you want to wait? "))
                profit = int((rate/100)*money)
                print("After this period you will get", profit, "extra money.")
                now = datetime.now()
                deposits[index] +=str(money) + "," + str(rate)+ "," +str(now)+ ";"
                a = False
        except ValueError: print("Incorrect number")
    for x in range(0, len(deposits)):
        deposits[x] += "\n"
    user_bank_deposit = open("user_bank_deposit.txt", "w")
    print(deposits)
    user_bank_deposit.writelines(deposits)
    users[index].set_money(users[index].get_money()-money)
    user_bank_deposit.close()
    return a

def month_changer(month):
    if month == "1":days = 0
    elif month =="2":days = 31
    elif month =="3":days = 59
    elif month =="4":days = 90
    elif month =="5":days = 120
    elif month =="6":days = 151
    elif month =="7":days = 181
    elif month =="8":days = 212
    elif month =="9":days = 243
    elif month =="10":days = 273
    elif month =="11":days = 304
    elif month =="12":days = 335
    return days

def deposit_checker(index, users):
    now = datetime.now()
    now = re.split("[\ \:\,\-\.]", str(now))
    time_now = int(now[0])*365*24*60 + month_changer(now[1])*24*60 + int(now[2])*24*60 + int(now[3])*60+ int(now[4])
    user_bank_deposit = open("user_bank_deposit.txt", "r")
    deposits = user_bank_deposit.readlines()
    deposits_info = re.split("\;", deposits[index])
    try:
        for x in range (len(deposits_info)):
            deposits_info[x] = re.split("\,", deposits_info[x])
        for x in range(len(deposits_info)):
            for y in range(len(deposits_info[x])):
                deposits_info[x][y]= re.split("[\ \:\,\-\.]", deposits_info[x][y])
        print("Your deposits: ")
        for x in range (len(deposits_info)-1):
            print("\nNUMBER", x+1, ":")
            print("Value :", deposits_info[x][0][0], "$")
            print("Rate :", deposits_info[x][1][0]+ "%")
            print("Date:", deposits_info[x][2][0] + ":" + deposits_info[x][2][1] + ":" + deposits_info[x][2][2] + " , " + deposits_info[x][2][3]+ ":" + deposits_info[x][2][4])
        for x in range(len(deposits_info)-1):
            time_then = int(deposits_info[x][2][0])*365*24*60 + month_changer(deposits_info[x][2][1])*24*60 +int(deposits_info[x][2][2])*24*60 + int(deposits_info[x][2][3])*60 + int(deposits_info[x][2][4])
            if time_now - time_then > int(deposits_info[x][1][0])*365*24*60:
                users[index].set_money(users[index].get_money()+int(int(credits_info[x][0][0])*(1+(int(credits_info[x][1][0])/100))))
                print("Congratulation, you've got some extra coins!  ")
                del deposits_info[x]
    except IndexError: pass
    user_bank_deposit = open("user_bank_deposit.txt", "w")
    user_bank_deposit.writelines(deposits_info)
    user_bank_deposit.close()
def credit_checker(index, users):
    now = datetime.now()
    now = re.split("[\ \:\,\-\.]", str(now))
    time_now = int(now[0])*365*24*60 + month_changer(now[1])*24*60 + int(now[2])*24*60 + int(now[3])*60+ int(now[4])
    user_bank_credit = open("user_bank_credit.txt", "r")
    credits = user_bank_credit.readlines()
    credits_info = re.split("\;", credits[index])
    try:
        for x in range (len(credits_info)):
            credits_info[x] = re.split("\,", credits_info[x])
        for x in range(len(credits_info)):
            for y in range(len(credits_info[x])):
                credits_info[x][y]= re.split("[\ \:\,\-\.]", credits_info[x][y])
        print("Your credits: ")
        for x in range (len(credits_info)-1):
            print("\nNUMBER", x+1, ":")
            print("Value :", credits_info[x][0][0], "$")
            print("Rate :", credits_info[x][1][0]+ "%")
            print("Date:", credits_info[x][2][0] + ":" + credits_info[x][2][1] + ":" + credits_info[x][2][2] + " , " + credits_info[x][2][3]+ ":" + credits_info[x][2][4])
        for x in range(len(credits_info)-1):
            time_then = int(credits_info[x][2][0])*365*24*60 + month_changer(credits_info[x][2][1])*24*60 +int(credits_info[x][2][2])*24*60 + int(credits_info[x][2][3])*60 + int(credits_info[x][2][4])
            if time_now - time_then > int(credits_info[x][1][0])*365*24*60:
                users[index].set_money(users[index].get_money()-int(int(credits_info[x][0][0])*(1+(int(credits_info[x][1][0])/100))))
                if users[index].get_money() >= 0:
                    print("Congratulation, you have paid off your credit yet!  ")
                else:
                    print("You have paid your credit off but now you have one credit more because you didnt have enough money")
                    credits[index].rstrip() +=str((-users[index].get_money()) + "," + str(10) + "," + str(now) + ";"+ "\n")
                    users[index].set_money(0)
                del credits_info[x]
    except IndexError: pass
    user_bank_credit = open("user_bank_credit.txt", "w")
    user_bank_credit.writelines(credits_info)
    user_bank_credit.close()
def credit(index, a, users):
    user_bank_credit = open("user_bank_credit.txt", "r")
    credits = user_bank_credit.readlines()
    for x in range(0, len(credits)):
        credits[x] = credits[x].rstrip()
    money = None
    while money == None:
        try: 
            money = int(input("How much money do want to get? if you want to return click 0: "))
            if money >0:
                rate = int(input("After how many days you will be able to return it? "))
                profit = int((rate/100)*money)
                print("After this period you will have to return", profit, "extra money.")
                now = datetime.now()
                print(credits)
                credits[index] +=str(money) + "," + str(rate) + "," + str(now) + ";"
                a = False
        except ValueError: print("Incorrect number")
    for x in range(0, len(credits)):
        credits[x] += "\n"
    user_bank_credit = open("user_bank_credit.txt", "w")
    user_bank_credit.writelines(credits)
    users[index].set_money(users[index].get_money()+money)
    user_bank_credit.close()
    return a

index = 4
a = 3
credit_checker(index)







def main(index):
    from mainprogram import users

    print("""
    Here you can save your money and after few days receive more, or take a loan but then you have to return us some bonus coins.
    1 - make a deposit
    2 - take a loan""")
    a = True
    while a:
        click = input("What do you want to do? write 1 or 2 ")
        if click == "1":
            a = deposit(index, a, users)
        if click == "2":
            a = credit(index, a, users)
        else:
            print("Incorrect choice..")
    