board_index = []
import random
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
    for x in range (0, 1500):
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


def get_board():
    for x in range(0, 40):
        for y in range(0, 65):
            print(board_index[x][y], end ="")
        print("")
    


board_create()
get_board()

