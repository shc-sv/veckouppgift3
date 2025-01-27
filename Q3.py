# Veckouppgift 3
# Q3: Kvittouträknaren

# Version 1
def q3_version1():
    print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit eller avsluta")
    summa = 0
    amount = input("Skriv in ett belopp: ")
    while amount.lower() not in ("quit", "avsluta"):
        # amount.casefold() är mer säkrare än .lower()
        try:
            amount = int(amount)
            summa += int(amount)
        except ValueError:
            print(f"{amount} är inte ett tal.")

        amount = input("Skriv in ett belopp: ")
    print(f"Det blir {summa} kr totalt. Välkommen åter!")

def q3_version2_3():
    # Version 1
    persons = input("Hur många är ni? Ange siffra här: ")
    while not persons.isdigit():
        persons = input("Hur många är ni? Ange siffra här: ")
    total = int(persons) * 25
    print(f"Det blir {total} kr totalt, alltså 25.0 kr per person.")

    # Version 2
    tip_percentage = input("Hur många procent dricks vill du lägga till? Ange här (%): ")

    if tip_percentage == "":
        tip_percentage = "10"
    else:
        while not tip_percentage.isdigit():
            tip_percentage = input("Hur många procent dricks vill du lägga till? Ange här (%): ")

    total = round(total *(1+float(tip_percentage)/100), 2)
    print(f"Total summa inkl. dricks: {total} kr . Välkommen åter!")