# Veckouppgift 3
# Q1: Diskutera i grupp

# Q1: 1)
def uppgift1():
    limit = 15
    index = 5
    while index <= limit:
        print(index)
        index +=2
# Q1: 2)
def uppgift2():
    # range(3): 0, 1, 2
    # range(star, stop, steg). range(3, 6) = 3, 4, 5 (6 är inte inkluderade)
    for i in range(10):
        if i == 5:
            print("")
        else:
            print(i)
        i += 1

# Q1: 3)
def uppgift3():
    counter = 0
    # i = 0, 1, 2, 3, 4, 5
    for i in range(6):
        counter += i
    print(counter)

# Q1: 4)
def uppgift4():
    x = 0
    y = 1

    # y = 1,.....9
    while y < 10:
        # % betyder resten vid division

        if y % 2 == 0:
            # y = 2, 4, 6, 8
            # x = x - y
            x -= y
        else:
            # y = 1, 3, 5, 7, 9
            # x = x + y * y
            x += y * y
        print_x_y(x, y)
        y += 1

def print_x_y(x, y):
    print(f"x = {x}, y = {y}.")

# Q1: 5)
def uppgift5():
    message ="its_time_to_get_coding"
    print(message[3:7])
    print(message[4:8])

# Q1: 6)
def uppgift6():
    for y in range(1,7):
        s = ""
        for x in range(1, 9):
            if x == y:
                s += "#"
            else:
                s += "."
        print(s)

    # Flytta linjen ett steg åt hörger
    for y in range(1,7):
        s = ""
        for x in range(1, 9):
            if x - y == 1:
                s += "#"
            else:
                s += "."
        print(s)