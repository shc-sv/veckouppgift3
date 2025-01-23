# Veckouppgift 3
# Q2: Öva på loopar och listor

# Q2 1a):
def q2_1a():
    print("1a:")
    answer = 0
    for i in range(11):
        # or range(1, 11), means 0,...10, stop: 11 is not included
        answer += i
    print("Summan av talen 1 till 10 är: " + str(answer))

# Q2 1b):
def q2_1b():
    print("1b:")
    answer = 0
    for i in range(101):
        answer += i
    print("For loop: Summan av talen 1 till 100 är: " + str(answer))

# Q2 1c):
def q2_1c():
    print("1c:")
    answer = 0
    i = 1
    while i < 101:
        answer += i
        i += 1
    print("While Loop: Summan av talen 1 till 100 är: " + str(answer))

# Q2 2):
def q2_2():
    print("2:")
    # Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]
    element_list = [1, -2, 3, -2, 4, -3]
    answer = 0
    for i in element_list:
        answer += i
        # print(f"i = {i}, answer = {answer}.")
    print(f"Summan av alla elementen i listan: [1, -2, 3, -2, 4, -3] är {answer}.")

# Q2 3):
def q2_3():
    # 3a):
    print("3a:")
    films = ["The Godfather", "Titanic", "Star Wars", "Alien"]
    print(f"Här är listan av fyra filmer: {films}.")

    # 3b):
    print("3b:")
    films.append("Fellowship of the ring")
    print(f"Filmen 'Fellowship of the ring' har lagts sist i listan: {films}.")

    # 3c):
    print("3c:")
    films.insert(0, "The two towers" )
    print(f"Filmen 'The two towers' har lagts på första platsen i listan: {films}.")

    '''
    # Testa .copy() 
    films = []
    films = films.copy()
    '''
    '''
    # Testa utan att använda insert()
    new_films = ["The two towers"]
    i = 1
    for i in range(len(films)):
        new_films.append(films[i])
    '''

    # 3d):
    print("3d:")
    position = films.index("Fellowship of the ring")
    print(f"Filmen 'Fellowship of the ring' har index {position} i listan.")

    # 3e):
    print("3e:")
    remove_element = "Titanic"
    films.remove(remove_element)
    position = films.index("Fellowship of the ring")
    print(f"Ta bort filmen {remove_element}. Filmen 'Fellowship of the ring' har nu index {position} i listan.")
    print(f"Här är ny filmlistan: {films}.")

    # 3f):
    print("3f:")
    list_length = len(films)
    print(f"Det finns {list_length} filmer i listan.")

    # 3g):
    print("3g:")
    films.reverse()
    print(f"Vänd listan baklänges. Nu ser filmlistan ut så här: {films}.")

    # 3h):
    print("3h:")
    films.sort()
    print(f"Sortera listan stigande i bokstavsordning. Nu ser filmlistan ut så här: {films}.")