import random


def main():
    summary = []

    while (True):
        action = input("What do you want to do now?\nType 0 for help\n")
        try:
            action = int(action)
        except ValueError:
            print("I'm sorry, I don't understand that")

        if action == 0:
            print("Help is here!\nType 0 for help (but you already knew that)\nType 1 to add a new type of unit and generate it's initiative\nType 2 to assemble and sort the generated units' initiatives and exit\nType 3 to exit immediately")
        elif action == 1:
            summary.extend(makeList())
            print(summary)
        elif action == 2:
            assembleList(summary)
            break
        elif action == 3:
            break







def makeList():
    #initilize variables
    initiativeList = []
    unitName = input("What is their name? ")
    modifier = int(input("What is their modifier? "))
    unitNumber = int(input("How many of them are there? "))
    #iterates unitNumber times to populate the list
    for i in range(unitNumber):
        d20 = random.randint(1, 20)
        initiative = d20 + modifier
        #adds a leading zero for sorting purposes
        if initiative < 10:
            initiative = "0" + str(initiative)

        unit = str(initiative) + " " + unitName.rstrip() + str(i+1)
        initiativeList.append(unit)

    return initiativeList


def assembleList(summary):
    None
    summary.sort(reverse=True)

    #inverts the list because it has to be made the other way to sort it easily
    for i in range(len(summary)):
        _ = summary[i][:3]
        __ = summary[i][3:]
        summary[i] = __ + " " + _
                
    #prints every calculated initiative
    for i in summary:
        print(i)

#a safety feature, probably overkill for this application
if __name__ == "__main__":
    main()