c = 0
from random import randint
print("Thank you for playing tapg. Please enter your password from save. Type in 000000 to start a new game. /n")
def game():
    c = input("Would you like to hear the controls? (Y/N)")
    if c = "Y":
        print("Type u to move up, d to move down, l to move left ,and r to move right. /n Type f to fight, m to use magic, h to heal, and s to save") 
    area = 0
    while 1:
        m = input()
        if m = "u":
            area = area + 1
        elif m = "l":
            area = area + 2
        elif m = "d":
            area = area + 3
        elif m = "r":
              area = area + 4
    while 1:
        if (area = 0 and (m = "d" or m = "r")) or (area = 62 and (m = "l" or m = "d")) or (area = 31 and (m = "u" or m = :
              print("Invalid move") 
