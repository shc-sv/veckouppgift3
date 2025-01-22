# Veckouppgift 3
# Q2: Öva på loopar och listor

# Q2 1a):
def q2_1a():
    answer = 0
    for i in range(11):
        # or range(1, 11), means 0,...10, stop: 11 is not included
        answer += i
    print("Summan av talen 1 till 10 är: " + str(answer))

# Q2 1b):
def q2_1b():
    answer = 0
    for i in range(101):
        answer += i
    print("For loop: Summan av talen 1 till 100 är: " + str(answer))

# Q2 1c):
def q2_1c():
    answer = 0
    i = 1
    while i < 101:
        answer += i
        i += 1
    print("While Loop: Summan av talen 1 till 100 är: " + str(answer))

def q2_2():
    # Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]
    element_list = [1, -2, 3, -2, 4, -3]
    answer = 0
    for i in element_list:
        answer += i
        # print(f"i = {i}, answer = {answer}.")
    print(f"Summan av alla elementen i listan: [1, -2, 3, -2, 4, -3] är {answer}.")
