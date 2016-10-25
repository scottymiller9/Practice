import random

def takechoice():
    print(random.randint(1, 6))
    choice = input("Want to roll again?")
    if choice == "yes" or choice == "Yes" or choice == "y" or choice == "Y":
        takechoice()

takechoice()
