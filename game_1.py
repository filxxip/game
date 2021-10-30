import random

def gra(index):
    from mainprogram import cleaar
    from mainprogram import User, users
    print("""
    Rules are so easy, you have give some money to start your game and there is 50 percent for double your bid and 50 percent for lose everything.
    You can stop your game in every moment and keep your win. """)
    bid = None
    while bid == None:
        try:
            bid = int(input("BID : "))
            cleaar()
            if bid > users[index].get_money(): print("You dont have enough money..")
            else: users[index].set_money(users[index].get_money()-bid)
        except ValueError: print("Incorrect value..")
    turn = True
    while turn:
        print("BID :", bid)
        if bid>0:
            question = input("Do you keep playing? ")
            if question == "yes":
                win = random.randrange(0, 2)
                if win == 0 : bid*=2
                elif win == 1 : bid = 0
            elif question =="no":
                turn = False
                print("Congrats, you have won", bid, "money")
            else: print("I dont understand")
        else: 
            print("Thanks for game")
            turn = False
    users[index].set_money(users[index].get_money()+bid)

