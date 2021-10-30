import random
import time
class Card(object):
    def __init__(self, value1, value2):
        self.__value1 = value1
        self.__value2 = value2
        self.set_prize_index()
    def get_value1(self):
        return self.__value1
    def get_value2(self):
        return self.__value2
    def get_prize_index(self):
        return self.__prize_index
    def set_prize_index(self):
        dictionary = {"2":0.01, "3":0.05, "4":0.1, "5":0.1, "6":0.15, "7":0.15, "8":0.2, "9":0.2, "10":0.25, "J":0.35, "D":0.5, "K":0.6, "As":0.8}
        for x in dictionary:
            if self.__value1 == x:
                self.__prize_index = dictionary[x]


def game_principle():
    print("""
    GAME 'Give Your Cards' principles:
    At the beggining of game you get random 4 cards and you have to give some money. Your potencial win will be dependent on them.
    After that you can change your card 3 times, but you dont have to obviously.
    Prize index:
    "2" - 0.01 of bid
    "3" - 0.05 of bid
    "4" - 0.1 of bid
    "5" - 0.1 of bid
    "6" - 0.15 of bid
    "7" - 0.15 of bid
    "8" - 0.2 of bid
    "9" - 0.2 of bid
    "10" - 0.25 of bid
    "J" - 0.35 of bid
    "D" - 0.5 of bid
    "K" - 0.6 of bid
    "As" - 0.8 of bid
    if you have 2 the same cards you get 2xprize index
    if you have 3 the same cards you get 4xprize index
    if you have 4 the same cards you get 8xprize index
    if you have 2 the same card value you get 10 percent more of your win
    if you have 3 the same card value you get 20 percent more of your win
    if you have 4 the same card value you get 40 percent more of your win

    Good luck! """
    )

cards = []
your_cards = []
def get_your_cards():
    hand = "Your cards: "
    for x in range(0, 5):
        hand += your_cards[x].get_value1()
        hand += your_cards[x].get_value2()
        hand +=", "
    return hand

def get_your_win(bid):
    win = 0
    for x in range (0, 5):
        win += your_cards[x].get_prize_index()
    help = []
    for x in range(0, 5):
        help.append(your_cards[x].get_value1())

    for x in range(0, 5):
        try:
            number = help.count(help[x])
            if number == 2:
                win += your_cards[x].get_prize_index()*2
                for y in range(0,2) : help.remove(help[x])
            elif number == 3:
                win += your_cards[x].get_prize_index()*6
                for y in range (0, 3):help.remove(help[x])
            elif number == 4:
                win += your_cards[x].get_prize_index()*14
                for y in range(0, 4):help.remove(help[x])
        except IndexError:
            pass
    return round(win*bid)

def deck_create():
    for x in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "D", "K", "As"):
        for y in ("Pik", "Trefl", "Kier", "Karo"):
            cards.append(Card(x, y))
def gra2(index):
    from mainprogram import cleaar
    from mainprogram import User, users
    game_principle()
    deck_create()
    bid = None
    while bid == None:   
        try : bid = int(input("Your bid: "))
        except ValueError : pass
    for a in range(0, 5):
        next = random.choice(cards)
        your_cards.append(next)
        cards.remove(next)
    for b in range(0, 3):
        cleaar()
        print(get_your_cards())
        print("Your win: ", get_your_win(bid))
        change = None
        while change == None:
            try: 
                change = int(input("\nWhich card you want to change if none write 0: "))
                if change < 0 or change > 5: change = None
            except ValueError : pass
        next = random.choice(cards)
        cards.remove(next)
        if change != 0: your_cards[change-1] = next
        else: break
    if change != 0:
        print(get_your_cards())
    print("Your win: ", get_your_win(bid))
    time.sleep(3)
    users[index].set_money(users[index].get_money() + get_your_win(bid))
    cards.clear()
    your_cards.clear()
        

