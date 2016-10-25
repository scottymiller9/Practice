import random

def checkinput():
    try:
        choice = int(input("Guess the number!"))
    except:
        print("You must enter an integer!")
        checkinput()
    if choice == randnum:
        print("Success!")
        quit()

    elif choice > randnum:
        print("Lower!")
        checkinput()
    else:
        print("Higher!")
        checkinput()


randnum = random.randint(1, 100)




checkinput()
