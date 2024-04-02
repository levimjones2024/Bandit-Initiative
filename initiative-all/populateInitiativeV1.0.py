import random


def main():


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
    initiativeList.sort(reverse=True)

    #inverts the list because it has to be made the other way to sort it easily
    for i in range(len(initiativeList)):
        _ = initiativeList[i][:3]
        __ = initiativeList[i][3:]
        initiativeList[i] = __ + " " + _

    #prints every calculated initiative
    for i in initiativeList:
        print(i)
                

#a safety feature, probably overkill for this application
if __name__ == "__main__":
    main()