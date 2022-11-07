
import numpy

def winer(table):
    if table[0][0] == table[0][1] == table[0][2] or table[1][0] == table[1][1] == table[1][2] or table[2][0] == table[2][1] == table[2][2] or table[0][0] == table[1][1] == table[2][2] or table[0][2] == table[1][1] == table[2][0]:
        return True

def play():
    p1 = input("Enter Name : ")
    p2 = input("Enter Name : ")
    print(f"First player is {p1}")
    print(f"Second player is {p2}")

    turn = 0

    table = numpy.array([["1","2","3"],["4","5","6"],["7","8","9"]])
    while True:
        if turn == 0:
            turn = 1
            inp = [int(i) for i in input(f"{p1} enter the postion of X : ").split()]
            pos1 = inp[0]
            pos2 = inp[1]
            if table[pos1][pos2] == "O":
                print(f"You loose one Chance {p1}")
            else:
                table[pos1][pos2] = "X"
            print(table)
            if winer(table) == True:
                print(f"{p1} wins..")
                break
        if turn == 1:
            turn = 0
            inp = [int(i) for i in input(f"{p2} enter the postion of 0 : ").split()]
            pos1 = inp[0]
            pos2 = inp[1]
            if table[pos1][pos2] == "X":
                print(f"You loose one Chance {p2}")
            else:
                table[pos1][pos2] = "O"
            print(table)
            if winer(table) == True:
                print(f"{p2} wins..")
                break

play()