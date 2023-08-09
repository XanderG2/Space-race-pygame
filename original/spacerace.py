import os, time, math, json, random

def displayUpgrades():
    print(",\n".join(list(f"{key}: {val}" for key,val in upgrades.items())))

def upgradef():
    global money
    displayUpgrades()
    print("Which upgrade would you like to upgrade?")
    upgrade = input("> ")
    if upgrade in upgrades.keys():
        if upgrade not in ["Name", "Level"]:
            if upgrade in ["Thrusters","Navigation","Cargo"]:
                os.system("cls" if os.name == "nt" else "clear")
                if upgrades[upgrade] >= 5:
                    print("Too high level.")
                else:
                    if money >= 5:
                        print(f"{upgrade} is being upgraded. please wait 10 seconds...")
                        time.sleep(10)
                        upgrades[upgrade] += 1
                        print(f"The {upgrade} upgrade is now at level {upgrades[upgrade]}.")
                        money -= 5
                    else:
                        print("No money")
            elif upgrade in ["Shields", "Resource scanning", "Research"] and upgrades["Level"] >= 3:
                os.system("cls" if os.name == "nt" else "clear")
                if money >= 20:
                    print(f"{upgrade} is being upgraded. please wait 10 seconds...")
                    time.sleep(10)
                    upgrades[upgrade] += 1
                    print(f"The {upgrade} upgrade is now at level {upgrades[upgrade]}.")
                    money -= 20
                else:
                    print("No money")
            elif upgrade in ["Weapons","Drones"] and upgrades["Level"] > 10:
                os.system("cls" if os.name == "nt" else "clear")
                if money >= 40:
                    print(f"{upgrade} is being upgraded. please wait 10 seconds...")
                    time.sleep(10)
                    upgrades[upgrade] += 1
                    print(f"The {upgrade} upgrade is now at level {upgrades[upgrade]}.")
                    money -= 40
                else:
                    print("No money.")
            else:
                print("Too low level. Need level 3 for shields,resource scanning, and research, and 10 for weapons and drones.")
        else:
            print(f"{upgrade} is not an upgrade")
    else:
        print(f"{upgrade} is not in upgrades")
        time.sleep(0.3)

def launch():
    os.system("cls" if os.name == "nt" else "clear")
    discoveredPlanets = []
    for level in range(1,upgrades["Navigation"]+1):
        for n in range(len(Planets[level])):
            discoveredPlanets.append(Planets[level][n])
    print("\n".join(list(f"{n+1}. {discoveredPlanets[n]}" for n in range(len(discoveredPlanets)))))
    print("Where would you like to launch to?")
    launchdestination = int(input("> "))-1
    launchdestination = discoveredPlanets[launchdestination]
    os.system("cls" if os.name == "nt" else "clear")
    print(f"The {shipname} is launching to {launchdestination}...")
    for n in range(1,11)[::-1]:
        print(n)
        time.sleep(1)
    print("Blast off!")
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")
    print(f"You are travelling to {launchdestination}.")
    if launchdestination in Planets[1]:
        print(f"please wait {math.floor(5/upgrades['Thrusters'])} seconds.")
        tier = 1
        time.sleep(5/upgrades["Thrusters"])
    elif launchdestination in Planets[2]:
        print(f"please wait {math.floor(10/upgrades['Thrusters'])} seconds.")
        tier = 2
        time.sleep(10/upgrades["Thrusters"])
    elif launchdestination in Planets[3]:
        print(f"please wait {math.floor(15/upgrades['Thrusters'])} seconds.")
        tier = 3
        time.sleep(15/upgrades["Thrusters"])
    elif launchdestination in Planets[4]:
        print(f"please wait {math.floor(30/upgrades['Thrusters'])} seconds.")
        tier = 4
        time.sleep(30/upgrades["Thrusters"])
    elif launchdestination in Planets[5]:
        print(f"please wait {math.floor(35/upgrades['Thrusters'])} seconds.")
        tier = 5
        time.sleep(35/upgrades["Thrusters"])
    print("You are here!")
    time.sleep(0.5)
    planetexplore(launchdestination, tier)

def planetexplore(planet, tier):
    global foundResources
    os.system("cls" if os.name == "nt" else "clear")
    upgrades["Level"] += 1
    print(f"Welccome to {planet}. {'Scan for resources?' if upgrades['Resource scanning'] > 0 else 'Look for resources?'}")
    if input("> ") == "yes":
        while True:
            if upgrades["Cargo"]*5 <= len(foundResources):
                print("You ran out of inventory space. Please sell items or upgrade cargo.")
                time.sleep(3)
                break
            if upgrades["Resource scanning"] > 0:
                print("Scanned for resources")
            else:
                print("Looking for resources...")
                time.sleep(2)
            if upgrades["Drones"] > 0:
                for drone in range(upgrades["Drones"]+1):
                    if tier == 1:
                        found = random.choice(tier1)
                        foundResources.append(found)
                    elif tier == 2:
                        found = random.choice(tier2)
                        foundResources.append(found)
                    elif tier == 3:
                        found = random.choice(tier3)
                        if found == "Alien":
                            if upgrades["Weapons"] > 0:
                                print("Your drones found an alien. They killed them.")
                                foundResources.append(found)
                            else:
                                print("Your drones found an alien. You had no weapons, so it killed the drone. You have lost 1 drone.")
                                upgrades["Drones"] -= 1
                    elif tier == 4:
                        found = random.choice(tier4)
                        foundResources.append(found)
                    elif tier == 5:
                        found = random.choice(tier5)
                        foundResources.append(found)
            else:
                if tier == 1:
                    found = random.choice(tier1)
                    foundResources.append(found)
                elif tier == 2:
                    found = random.choice(tier2)
                    foundResources.append(found)
                elif tier == 3:
                    found = random.choice(tier3)
                    if found == "Alien":
                        if upgrades["Weapons"] > 0:
                            print("You found an alien. You killed them.")
                            foundResources.append(found)
                        else:
                            print("You found an alien. You had no weapons, so it killed you. You have lost your inventory and have been reset back to Earth.")
                            foundResources = []
                            time.sleep(3)
                            break
                elif tier == 4:
                    found = random.choice(tier4)
                    foundResources.append(found)
                elif tier == 5:
                    found = random.choice(tier5)
                    foundResources.append(found)
            if upgrades["Drones"] > 0:
                print(f"Your drones have found {', '.join(foundResources)}\nDo you want to scan for more?")
                if input("> ") != "yes":
                    break
            elif upgrades["Resource scanning"] > 0:
                print(f"You have found {', '.join(foundResources)}\nDo you want to scan for more?")
                if input("> ") != "yes":
                    break
            else:
                print(f"You have found {', '.join(foundResources)}\nDo you want to look for more?")
                if input("> ") != "yes":
                    break
            os.system("cls" if os.name == "nt" else "clear")
    else:
        print("Ok")
    print("You are at Earth")

def inventory():
    global money
    os.system("cls" if os.name == "nt" else "clear")
    print(f"You have {money} money.")
    print(", ".join(foundResources))
    print("Sell item?")
    sell = input("> ")
    if sell == "yes":
        os.system("cls" if os.name == "nt" else "clear")
        for item in range(len(foundResources)):
            print(f"{item+1}. {foundResources[item]}. Sell for {prices[foundResources[item]]}")
        sellitem = int(input("> "))-1
        money += prices[foundResources[sellitem]]
        foundResources.pop(sellitem)

def research():
    global researchedMaterials, foundResources
    os.system("cls" if os.name == "nt" else "clear")
    if upgrades["Research"] > 0:
        print("What would you like to research?")
        researchoptions = list(set(foundResources))
        for option in range(len(researchoptions)):
            print(f"{option+1}. {researchoptions[option]}")
        try:
            researchinginput = int(input("> "))-1
            if researchinginput in range(len(researchoptions)):
                researching = researchoptions[researchinginput]
                if researching not in unresearchable:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"Researching {researching}...")
                    time.sleep(20/upgrades["Research"])
                    print(f"{researching} researched! You have created {researchedMaterials[researching]}!")
                    found = False
                    index = 0
                    while not found:
                        if foundResources[index] == researching:
                            found = True
                            break
                        index += 1
                    try:
                        foundResources.pop(index)
                    except: print(f"Index too large. {index}")
                    try:
                        foundResources.append(researchedMaterials[researching])
                    except:
                        try:
                            print(f"Could not append. {index}/ {researching}/ {researchedMaterials[researching]}")
                        except:
                            print("Error in printing error message.")
                else:
                    print(f"{researching} is too high tier to research. Sell or keep it.")
            else:
                print("Must be one of the options.")
        except ValueError:
            print("Must be a number")
    else:
        print("Upgrade reseach skill first.")
    time.sleep(3)

def saveprep():
    os.system("cls" if os.name == "nt" else "clear")
    print("What save name would you like to use?")
    filename = input("> ")
    filepath = "spacerace saves/" + filename + ".space" #make a folder called spacerace saves
    print("Save as "+filename+".space?")
    overwrite = input("> ")
    if overwrite == "yes":
        save(filepath)
    else:
        saveprep()

def save(filepath):
    global upgrades,money,foundResourcess
    with open(filepath, "w") as f:
        stats = str(upgrades)+"\n"+str(money)+"\n"+"/".join(foundResources)
        f.write(stats)
    exit()

def loadprep():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n".join(os.listdir("spacerace saves")))
    print("What is the name of the file?")
    filename = input("> ")
    if filename in os.listdir("spacerace saves"):
        load(filename)
    else:
        print("Not a file. Try again")
        loadprep()

def load(filename):
    global upgrades, money, foundResources
    filepath = "spacerace saves/" + filename #make a folder called spacerace saves
    try:
        with open(filepath, "r") as f:
            file = f.read().splitlines()

        upgrades = eval(file[0])
        money = int(file[1])
        if file[2] != "":
            foundResources = file[2].split("/")
        else:
            foundResources = []
    except:
        print("Corrupted file. Sorry!")
    
os.system("cls" if os.name == "nt" else "clear")
print("====================================================\n  Welcome to space race! The aim of the game is to\n    try to make it to space before everyone else.\n====================================================\n")
print("Enter your name!")
username = input("> ")

while True:
    print("Enter a name for your ship!")
    shipname = input("> ")
    if any(item in shipname for item in ["'", '"', "\\"]):
        print("Please try again. Do not use special characters in shipname.")
    else:
        break

upgrades = {
    "Name":shipname,
    "Level":1,
    "Thrusters":1,
    "Shields":0,
    "Navigation":1,
    "Cargo":1,
    "Weapons":0,
    "Resource scanning":0,
    "Research":0,
    "Drones":0
}

discoveredPlanets = []
foundResources = []

tier1 = ["Iron","Copper","Space rock","Water","Scraps","Nickel","Alien bacteria"]
tier2 = ["Iron","High quality space rock","Nickel","Small alien organism"]
tier3 = ["Unknown metal","Extremely high quality space rock","Alien"] #dont ask why aliens are being sold idk lol
tier4 = ["Unknown metal","Purple material","Alien DNA","Uranium"]
tier5 = ["Unknown new element","Green material","Alien architecture","Plutonium","Magic","Teleportation"]

researchedMaterials = {
    "Iron":"Scraps",
    "Copper":"Scraps",
    "Space rock":"Alien bacteria",
    "Water":"Copper",
    "Scraps":"Nickel",
    "Nickel":"Space rock",
    "Alien bacteria":"Alien DNA",
    "High quality space rock":"Small alien organism",
    "Small alien organism":"Alien DNA",
    "Unknown metal":"Unknown new element",
    "Extremely high quality space rock":"The highest quality space rock",
    "Alien":"High quality alien DNA",
    "Purple material":"Purple unknown new element",
    "Alien DNA":"High quality alien DNA",
    "High quality alien DNA":"Reconstructable ancient alien DNA",
    "Reconstructable ancient alien DNA":"Dinosaur alien",
    "Uranium":"Plutonium",
    "Green material":"Green unknown new element",
    "Alien architecture":"Alien blueprint",
    "Plutonium":"Green material",
    "Magic":"Teleportation",
    "Teleportation":"Teleporter",
    "Alien blueprint":"Alien house"
}

unresearchable = ["The highest quality space rock","Purple unknown new element","Dinosaur alien","Green unknown new element","Teleporter","Alien house"]

prices = {
    "Iron": 5,
    "Copper": 3,
    "Space rock": 15,
    "Water": 1,
    "Scraps": 6,
    "Nickel": 8,
    "Alien bacteria": 25,
    "High quality space rock": 25,
    "Small alien organism": 32,
    "Unknown metal":30,
    "Extremely high quality space rock": 35,
    "The highest quality space rock": 50,   #only unlockable through research
    "Alien": 40,
    "Purple material": 45,
    "Purple unknown new element": 70,   #only unlockable through research
    "Alien DNA": 50,
    "High quality alien DNA": 55,   #only unlockable through research
    "Reconstructable ancient alien DNA": 70,    #only unlockable through research
    "Dinosaur alien": 100,  #only unlockable through research
    "Uranium": 25,
    "Unknown new element": 65,
    "Green material": 65,
    "Green unknown new element": 75,    #only unlockable through research
    "Alien architecture": 65,
    "Alien blueprint": 70,  #only unlockable through research
    "Alien house": 85,  #only unlockable through research
    "Plutonium": 30,
    "Magic": 85,
    "Teleportation": 100,
    "Teleporter": 125  #only unlockable through research
}

money = 0

Planets = {
    1:["Mercury","Venus","Mars","Asteroid belt","Jupiter","Saturn","Uranus","Neptune","Pluto","Keiper Belt"],
    2:["Proxima centauri b", "Proxima centauri c", "Proxima centauri d"], #wikipedia closest stars
    3:["Epsilon Eridani b", "YZ Ceti b", "YZ Ceti c", "YZ Ceti d"],
    4:["HD 219134 b", "HD 219134 c", "HD 219134 d", "HD 219134 g", "HD 219134 h"],
    5:["SWEEPS-11", "SWEEPS-04", "COCONUTS-2b", "CT Chamaeleontis b"] #wikipedia furthest stars: sweeps11 sweeps04
}
os.system("cls" if os.name == "nt" else "clear")

print(f"Welcome aboard the {shipname}, {username}!")

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Do you want to 1. upgrade {shipname} or 2. launch it? or 3. see inventory or 4. research or 5. save and quit or 6. load")
    option = input("> ")
    if option == "1":
        upgradef()
    elif option == "2":
        launch()
    elif option == "3":
        inventory()
    elif option == "4":
        research()
    elif option == "5":
        saveprep()
    elif option == "6":
        loadprep()
