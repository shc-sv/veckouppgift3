# Veckouppgift 3
# Q5: Gissa talet
import random

def q5():
    print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100.")
    secret = random.randint(1, 100)
    count = 0
    print(f"Slumpmässigt tal är: {secret} ")
    while secret > 0:
        guess_number = input("Kan du gissa vilket det är? ")
        count += 1
        try:
            guess_number = int(guess_number)
            if 0 < guess_number <= 100:
                # Version 2: Check if you are close by guessing within 5 of the correct answer.
                near_correct = abs(secret-guess_number)

                if guess_number < secret:
                    print("Nej, det är för lågt!")
                    if near_correct <= 5:
                        print("Nu börjar det brännas!")
                elif guess_number > secret:
                    print("Nej, det är för högt!")
                    if near_correct <= 5:
                        print("Nu börjar det brännas!")
                else:
                    print(f"Det är rätt!! Du gjorde det på {count} gissningar.")
                    break
            else:
                print("Ange ett tal mellan 1 och 100.")

        except ValueError:
            print("Ange ett tal mellan 1 och 100.")

