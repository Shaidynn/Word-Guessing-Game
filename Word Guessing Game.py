import random

start = input("Would you like to play in easy, medium, or hard mode? ")

if start.lower() == "easy":
    Max = print("You have a maximum of 3 guesses.")
    maxguess = 3
    for i in range(0, maxguess):
        list = ["Grass", "Food", "Car", "House", "Lights"]
        pick = random.choice(list)
        correct = pick
        guess = input("Enter your guess here: ")
        if guess != correct or guess < maxguess:
            print("Please try again soon...") 
        elif guess == correct:
            print("~~~CONGRATULATIONS~~~")
            quit()
    if guess != correct and maxguess == 3:
            print(f"The word was {pick}! Better luck next time...")
            exit()
   
if start.lower() == "medium":
    Max2 = print("You have a maximum of 3 guesses.")
    maxguess2 = 3
    for y in range(0, maxguess2):
        list2 = ["Python", "Horror", "Molecule", "Canada", "Water"]
        pick2 = random.choice(list2)
        correct2 = pick2
        guess2 = input("Enter your guess here: ")
        if guess2 != correct2:
            print("Please try again...")
        elif guess2 == correct2:
            print("~~~CONGRATULATIONS~~~")
            break
    if guess2 != correct2 and maxguess2 == 3:
        print(f"The word was {pick2}! Better luck next time...")
        exit()
    
if start.lower() == "hard":
    Max3 = print("You have a maximum of 3 guesses.")
    maxguess3 = 3
    for x in range(0, maxguess3):
        list3 = ["Python", "Ecstasy", "Adventure", "Waterloo", "Journey"]
        pick3 = random.choice(list3)
        correct3 = pick3
        guess3 = input("Enter your guess here: ")
        if guess3 != correct3:
            print("Please try again...")
        elif guess3 == correct3:
            print("~~~CONGRATULATIONS~~~")
            break
    if guess3 != correct3 and maxguess3 == 3:
        print(f"The word was {pick3}! Better luck next time...")
        exit()

else:
    print("Invalid syntax. Try again later!")
