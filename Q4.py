# Veckouppgift 3
# Q4: Figurer med loopar

def q4():
    # a):
    print("a):")
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == 1:
                s += "#"
            else:
                s += "."
        print(s)

    # b):
    print("b):")
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == y:
                s += "#"
            else:
                s += "."
        print(s)

    # c):
    print("c):")
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x in (3, 4, 5):
                s += "#"
            else:
                s += "."
        print(s)

    # d):
    print("d):")
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == 3 or y==3:
                s += "#"
            else:
                s += "."
        print(s)

    # e):
    print("e):")
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            summa = x + y
            if x == 5 or summa == 7:
                s += "#"
            else:
                s += "."
        print(s)

    # f):
    print("f):")
    summa = 0
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            summa = x + y
            if x == y or summa == 7:
                s += "#"
            else:
                s += "."
        print(s)

    # g):
    print("g):")
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            modulus = x % 2
            if modulus != 0:
                s += "#"
            else:
                s += "."
        print(s)

    # h):
    print("h):")
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if (y in (3, 4) and x in (2, 7)) or (y in (2, 5) and x in (2, 3, 4, 5 ,6 ,7)):
                s += "#"
            else:
                s += "."
        print(s)

    # i):
    print("i):")
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            modulus_y = y % 3
            modulus_x = x % 3

            if (modulus_y == 1 and modulus_x == 1) or (modulus_y == 2 and modulus_x == 2) or (modulus_y == 0 and modulus_x == 0):
                s += "."
            elif (modulus_y == 1 and modulus_x == 2) or (modulus_y == 2 and modulus_x == 0) or (modulus_y == 0 and modulus_x == 1):
                s += "#"
            elif (modulus_y == 1 and modulus_x == 0) or (modulus_y == 2 and modulus_x == 1) or ( modulus_y == 0 and modulus_x == 2):
                s += "O"
        print(s)

    # j):
    print("j):")
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            modulus_3 = x % 3
            modulus_2 = x % 2
            if (y <= 3) and (modulus_3 == 0) or (y == 5 and modulus_2 == 0) or (y == 6 and modulus_2 == 0):
                s += "#"
            else:
                s += "."
        print(s)
