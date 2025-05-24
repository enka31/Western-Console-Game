import random

plrLocation = None
plrSkill = None
plrName = None
plrCoins = None
plrWater = 0
plrAction = None
srfRoom = None
randyrandom = None
horsewater = True
horseFood = True
gameStart = False

# Get player name once
print("Enter your name:")
plrName = input()
print(f"Hello {plrName}")
plrCoins = 3

# Get player skill once
print("Please Select A Skill for your character (Gambler, Shooter, Thief):")
while plrSkill not in ["Gambler", "Shooter", "Thief"]:
    plrSkill = input()
    if plrSkill in ["Gambler", "Shooter", "Thief"]:
        print(f"You selected your Skill as: {plrSkill}")
    else:
        print("Please enter one of the valid classes (Gambler, Shooter, Thief)")

def Slotmachine():
    global plrSkill, plrWater, plrCoins
    goagain = True
    while goagain:
        if plrCoins > 0:
            lackilacki = random.randrange(1, 100)
            plrCoins -= 1
            if plrSkill == "Gambler":
                if 1 < lackilacki < 55:
                    plrCoins += 2
                    print(f"You earned 2 Coins! Now you have: {plrCoins} Coins")
                elif lackilacki == 99:
                    plrCoins += 10**18  # Huge jackpot
                    print(f"JACKPOT! You are now rich with {plrCoins} coins!")
                else:
                    print(f"Sad Boi -1 You now have {plrCoins} Coins")
            else:
                if 1 < lackilacki < 50:
                    plrCoins += 2
                    print(f"You earned 2 Coins! Now you have: {plrCoins} Coins")
                elif lackilacki == 99:
                    plrCoins += 10**18
                    print(f"JACKPOT! You are now rich with {plrCoins} coins!")
                else:
                    print(f"Sad Boi -1 You now have {plrCoins} Coins")
            print("Go Again? (True / False)")
            goagaini = input()
            if goagaini != "True":
                goagain = False
        else:
            print("You have no money.")
            goagain = False

def buyWater():
    global plrCoins, plrWater
    if plrCoins > 0:
        plrCoins -= 1
        plrWater += 1
        print("You bought a water for 1 coin. It doesn't do anything though. Scam!")
    else:
        print("You don't have coins.")

def askloc():
    global plrLocation
    plrLocation = None
    while plrLocation not in ["Bar", "Sherrifs Office", "Stable"]:
        print("Select where do you want to go (Bar, Sherrifs Office, Stable):")
        plrLocation = input()
    print(f"You are going to {plrLocation}")

# Main game loop controlling horse food/water and locations
while horseFood or horsewater:
    gameStart = True

    # Assign Sheriff Office scenario if not assigned
    if srfRoom is None:
        randyrandom = random.randrange(1, 3)
        if randyrandom == 1:
            srfRoom = "Criminal"
        elif randyrandom == 2:
            srfRoom = "Sleep"

    askloc()

    if plrLocation == "Bar":
        plrAction = None
        while plrAction not in ["Slots", "Wotah"]:
            print("What do you want to do? (Slots, Wotah)")
            plrAction = input()
            if plrAction == "Wotah":
                buyWater()
                break  # Go back to location selection
            elif plrAction == "Slots":
                Slotmachine()
                break  # Go back to location selection

    elif plrLocation == "Sherrifs Office":
        if srfRoom == "Criminal":
            if plrSkill == "Shooter":
                randyrandom = random.randrange(1, 10)
                if randyrandom > 7:
                    print("A Criminal hiding in the office shot YOU!!! You are dead. You failed to feed your horse. Shame on you and your horse.")
                    break
                else:
                    plrCoins += 30
                    print(f"You found and killed a criminal hiding in Sheriff's Office. Sheriff rewarded you. Now you have {plrCoins} coins.")
                    srfRoom = "Empty"
            else:
                randyrandom = random.randrange(1, 3)
                if randyrandom >= 2:
                    print("A Criminal hiding in the office shot YOU!!! You are dead. You failed to feed your horse. Shame on you and your horse.")
                    break
                else:
                    plrCoins += 30
                    srfRoom = "Empty"
                    print(f"You found and killed a criminal hiding in Sheriff's Office. Sheriff rewarded you. Now you have {plrCoins} coins.")
            srfRoom = "Empty" 

        elif srfRoom == "Sleep":
            if plrSkill == "Thief":
                randyrandom = random.randrange(1, 10)
                if randyrandom > 7:
                    print("You tried to rob the sheriff while he was sleeping AND HE SHOT YOU!!! You are dead. You failed to feed your horse. Shame on you and your horse.")
                    break
                else:
                    plrCoins += 30
                    srfRoom = "Empty"
                    print(f"You found the sheriff sleeping and decided to go through his pockets. You found 30 coins! Now you have {plrCoins} coins.")
            else:
                randyrandom = random.randrange(1, 3)
                if randyrandom >= 2:
                    print("You tried to rob the sheriff while he was sleeping AND HE SHOT YOU!!! You are dead. You failed to feed your horse. Shame on you and your horse.")
                    break
                else:
                    srfRoom = "Empty"
                    plrCoins += 30
                    print(f"You found and killed a criminal hiding in Sheriff's Office. Sheriff rewarded you. Now you have {plrCoins} coins.")
            srfRoom = "Empty"  

        else:
            print("The Sheriff's Office seems quiet. Nothing happens.")
            srfRoom = None

    elif plrLocation == "Stable":
        plrAction = None
        print("Buy water for your horse 15C, Buy food for your horse 20C, or go back to town.")
        print("Water, Food, Back")
        while plrAction not in ["Water", "Food", "Back"]:
            plrAction = input()
            if plrAction == "Water":
                if plrCoins >= 15:
                    plrCoins -= 15
                    print(f"You bought water for your horse. You now have {plrCoins} coins.")
                    horsewater = False
                    break
                else:
                    print("Not enough money.")
                    plrAction = None  # Ask again
            elif plrAction == "Food":
                if plrCoins >= 20:
                    plrCoins -= 20
                    print(f"You bought food for your horse. You now have {plrCoins} coins.")
                    horseFood = False
                    break
                else:
                    print("Not enough money.")
                    plrAction = None  # Ask again
            elif plrAction == "Back":
                print("Going back to town.")
                break

while gameStart == True:

 if not (horseFood and horsewater):
    print("You won! You left the town using your scruffy donkey.")
 else:
    print("You lost yourself and your donkey. (You had to be a prostitute to earn money too.)")
 print("Do you Wanna Play Again(Yes, No)")
 gamegoagain = input()
 if gamegoagain == ("Yes"):
    gameStart = False
    horseFood = True
    horsewater = True
    plrCoins = 3
    plrSkill = None
    plrName = None
    plrAction = None
    plrLocation = None
 