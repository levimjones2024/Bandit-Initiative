import random


"""
README

This script works on Python 3.10.5, but should work with any version of python 3

Python itself can be found at https://www.python.org/downloads/windows/ (or you can find it yourself if you distrust links)

The script expects a plaintext file called "organize.txt" in the same directory as it with the names of each unit to be initiative'd on their own line.
"""

def main():
    #initilize variables
    initiativeList = []
    modifier = int(input("What modifier to use? ")) #I can't find the individual initiative for every creature, therefore you will have to separate them into batches with each initiative modifier. If you end up using a flat bonus for every NPC you can add a "#" to the start of this line and remove that same symbol in front of the line below this.
    #modifier = 1 #change this number

    #opens the file and ingests every line
    with open("organize.txt", "r") as file:
        for f in file:
            if f == "":
                None
            else:
                d20 = random.randint(1, 20)
                initiative = d20 + modifier
                #adds a leading zero for sorting purposes
                if initiative < 10:
                    initiative = "0" + str(initiative)

                unit = str(initiative) + " " + f.rstrip()
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