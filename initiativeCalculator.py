


def main():
    #initilize variables
    initiativeList = []

    #opens the file and ingests every line
    with open("organize.txt", "r") as file:
        for f in file:
            if f == "":
                None
            else:
                f = f.rstrip()
                _ = f[:3]
                __ = f[3:]
                f = __ + " " + _
                initiativeList.append(f)

        initiativeList.sort(reverse=True)

        #inverts the list because it has to be made the other way to sort it easily
        for i in range(len(initiativeList)):
            #print(initiativeList[i])
            _ = initiativeList[i][:3].strip()
            __ = initiativeList[i][3:]
            initiativeList[i] = __ + " " + _
            initiativeList[i] = initiativeList[i].strip()


        #prints every calculated initiative
        for i in initiativeList:
            print(i)
                

#a safety feature, probably overkill for this application
if __name__ == "__main__":
    main()