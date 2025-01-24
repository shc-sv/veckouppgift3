# Veckouppgift 3
# Q6: att göra-lista

def q6():
    todo_list = []
    finished_list =[]

    print("** Todo list extravaganza **")
    print("0. Avsluta")
    print("1. Se innehållet i din lista")
    print("2. Lägga till nya punkter i din lista")
    # Version 2
    print("3. Markera som klar")
    # Version 3
    print("4. Lägg tillbaka grejen i todo-listan")

    # While-loop fortsätter fråga användaren oavsett om ett giltigt alternativ väljs eller inte.
    # Tills: break (används för att bryta loop)
    while True:
        choice = input("Välj ett alternativ (mellan 0 och 4): ")
        if choice == '1':
            if not todo_list:
                print("Din todo-lista är tom!")
            else:
                print_list(todo_list)
        elif choice == '2':
            add_thing = input("Skriv in en ny sak som du måste komma ihåg att göra: ")
            todo_list.append(add_thing)
            print(f"Ok, {add_thing} lades till i listan. ")
        elif choice == '3':
            choice_made = False
            length = len(todo_list)

            # Om listan är tom, ska vi inte göra något här.
            if length > 0:
                print("Här är todo-listan. Vilken grej är du färdig med?")
                print_list(todo_list)

                # Om valet inte finns i listan (choice_made = False),
                # skriver vi ut ett felmeddelande och loopen fortsätter
                while not choice_made:
                    thing_index = input("Ange nummer här: ")
                    try:
                        thing_index = int(thing_index)
                        if 0 < thing_index <= length:
                            thing_index -= 1
                            remove_thing = todo_list[thing_index]
                            todo_list.remove(remove_thing)
                            print_list(todo_list)
                            choice_made = True

                            # Version 3
                            finished_list.append(remove_thing)
                        else:
                            print("Ogiltigt nummer, försök igen.")
                    except ValueError:
                        print("Ogiltigt nummer, försök igen.")
            else:
                print("Din todo-lista är tom!")
        elif choice == '4':
            length_finished = len(finished_list)
            if length_finished == 0:
                print("Ingen grej har bockats av tidigare.")
            else:
                print("De här grejerna har bockats av tidigare.")
                print_list(finished_list)
                for thing in finished_list:
                    todo_list.append(thing)
                print("Nu har grejerna lagts tillbaka i todo-listan!")
        elif choice == '0':
            print("Hej då!")
            break

# Viktigt!!
def print_list(my_list):
    # enumerate() är en praktisk funktion i Python som låter dig iterera över en lista samtidigt
    # som du får tillgång till både index och element.
    # Om man vill index börja med 1 istället: start = 1.
    for index, thing in enumerate(my_list, start=1):
        print(f"{index}. {thing}")
