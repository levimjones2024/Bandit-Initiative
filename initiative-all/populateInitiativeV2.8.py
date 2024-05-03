import random

#if you wish to use the health and damage aids alongside the initiative tracker, add them here with the format:
#"Name": [Health, attack-modifier, number-of-dice-rolled, size-of-dice, damage-modifier ]

NPCUnit = {
    "Bandit": [30, +3, 2, 8, 3],
    "null": [0, 0, 0, 0, 0,]
}

def main():
    summary = []


    while (True):
        action = safeMakeInt("What do you want to do now?\nType 0 for help\n")

        if action == 0:
            print("Help is here!\nType 0 for help (but you already knew that)\nType 1 to add a new type of unit and generate it's initiative\nType 2 to assemble and sort the generated units' initiatives\nType 3 to run initiative (requires an assembled list)\nType 4 to exit immediately")
        elif action == 1:
            summary.extend(makeList())
            print(summary)
        elif action == 2:
            prettyList, unitHealth = assembleList(summary)
            for i in prettyList:
                print(i)
        elif action == 3:
            runInitiative(summary, prettyList, unitHealth)
        elif action == 4:
            break


def runInitiative(summary, prettyList, unitHealth):
    initiativeCounter = 0


    while True:
        placeCounter = -1
        if initiativeCounter >= len(prettyList):
            initiativeCounter = 0

        for i in prettyList:
            placeCounter += 1
            attackRoll = ""
            damageRoll = 0
            unitUse = "null"
            d20Roll = 0

            for key in NPCUnit:
                if key in i:
                    unitUse = key


            if placeCounter == initiativeCounter:
                if "^" in i: #the "^" flag is an internal part that is printed to simplify development, it's presence indicates that the unit in question has a dictionary enrty.
                    d20Roll = random.randint(1, 20)
                    for j in range(NPCUnit[unitUse][2]):
                        damageRoll += random.randint(1, NPCUnit[unitUse][3])
                    damageRoll += NPCUnit[unitUse][4]
                    #crit detection, here using a tablerule called "crunchy crit" where you deal max possible damage from one roll of the dice, manually roll again, and add the two for actual crit damage.
                    if d20Roll == 20:
                        damageRoll += (NPCUnit[unitUse][2]*NPCUnit[unitUse][3]+NPCUnit[unitUse][4])
                        print(f"{f'{i} <---':<20}Health: {unitHealth[placeCounter]} ID: {placeCounter}" + f"     Attack Roll: CRITICAL HIT; Damage roll: {damageRoll}")
                    else:
                        attackRoll = d20Roll + NPCUnit[unitUse][1]
                        print(f"{f'{i} <---':<20}Health: {unitHealth[placeCounter]} ID: {placeCounter}" + f"     Attack Roll: {attackRoll}; Damage roll: {damageRoll}")
                else: 
                    print(f"{f'{i} <---':<20}Health: {unitHealth[placeCounter]} ID: {placeCounter}")

            else:
                print(f"{i: <20}Health: {unitHealth[placeCounter]} ID: {placeCounter}")

        #Initiative menu loop
        while True:
            userInput = input("Type 1 to quit\nType 2 to apply damage to a unit\nType 3 to add a new unit\nType 4 to continue initiative\n")
            if userInput == "1":
                quit()
            elif "2" in userInput:
                #get the health list and apply damage to the right unit
                while True:
                    whoAttack = safeMakeInt("Which ID to damage? ")
                    if whoAttack < len(prettyList):
                        howMuchDamage = safeMakeInt("How much damage? ")
                        unitHealth[whoAttack] = unitHealth[whoAttack] - howMuchDamage
                        break
                    else:
                        print("I don't know who that is!")
            elif userInput == "3":
                unitAdd = input("What is the name of the new unit? ")
                unitAddInitiative = safeMakeInt("What is their initiative? ")
                unitAdd = unitAdd + " " + str(unitAddInitiative)
                unitAddHealth = safeMakeInt("How much Health do they have? (0 if N/A) ")
                whereToAdd = -1

                for initiative in prettyList:
                    initiative = initiative[-3:]
                    whereToAdd += 1
                    if int(initiative) > int(unitAddInitiative):
                        print(whereToAdd, initiative)
                    else:
                        print("Found it", whereToAdd)
                        unitHealth.insert(whereToAdd, unitAddHealth)
                        prettyList.insert(whereToAdd, unitAdd)
                        break

            elif userInput == "4":
                break

        initiativeCounter += 1
    None

def safeMakeInt(mesaage):
    while True:
        toBeInt = input(mesaage)
        try:
            toBeInt = int(toBeInt)
            return toBeInt
        except ValueError:
            print("I don't know what that is!")


def makeList():
    #initilize variables
    initiativeList = []
    initiative = 0
    setInitiative = False
    unitName = input("What is their name? ")
    modifier = input("What is their modifier? (leave empty if initiative has already been rolled) ")
    try:
        modifier = int(modifier)
        unitNumber = int(input("How many of them are there? "))
    except ValueError:
        if modifier == "":
            initiative = int(input("What is their initiative? "))
            setInitiative = True
            unitNumber = 1
        else:
            print("This isn't a number!")
            quit()
    
    global NPCUnit

    #iterates unitNumber times to populate the list
    for i in range(unitNumber):
        d20 = random.randint(1, 20)
        if setInitiative == False:
            initiative = d20 + modifier
        #adds a leading zero for sorting purposes
        if initiative < 10:
            initiative = "0" + str(initiative)

        if unitName in NPCUnit.keys():
            unit = str(initiative) + " " + unitName.rstrip() + str(i+1) + "^"
        else:
            unit = str(initiative) + " " + unitName.rstrip() + str(i+1)
        initiativeList.append(unit)

    return initiativeList


def assembleList(summary):
    unitHealth = []
    global NPCUnit

    summary.sort(reverse=True)

    #inverts the list because it has to be made the other way to sort it easily
    for i in range(len(summary)):
        _ = summary[i][:3]
        __ = summary[i][3:]
        summary[i] = __ + " " + _
        if "^" in __:
            for key in NPCUnit.keys():
                if key in __:
                    unitHealth.append(NPCUnit[key][0])
        else:
            unitHealth.append(0)
            
                
    return summary, unitHealth

#a safety feature, probably overkill for this application
if __name__ == "__main__":
    main()