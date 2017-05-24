#should read in a file of dialoues and catalouge them into 1 of the four horsemen or coresponding good behaviours
"""
horsemen
1 - Critizim
2- Contempt
3 - defensiveness
4 - stonewalling
0 - unclassified
"""
import json

def main():
    horse_dictionary = readscript()
    write_horsemen(horse_dictionary)

def readscript():
    horses = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    if(input("Readfile  = 0, enterlines = 1 :") == '0'):
        filename = (input("please enter filename: ")+".txt")
        script = open(filename, 'r')
        print("\n classify lines into horsemen\n **********\n")
        for line in script:
            line = (line.strip('-')).strip()
            horse = int(input(str(line) + "\n"))
            horses[horse].append(line)
        script.close()
    else:
        print("\n classify lines into horsemen\n **********\n")
        enterline = input("Enter line of marital disagreement: ")
        while enterline != "-1":
            enterline = (enterline).strip()
            horse = int(input(str(enterline) + "\n"))
            horses[horse].append(enterline)
            enterline = input("Enter line of marital disagreement: ")

    for i in  range (len(horses)-1):
        print(i, end=" ")
        for words in horses[i]:
            print(words, end = " ")
        print()
    return horses

def write_horsemen(horsedict):
    print(json.dumps(horsedict))
    filename = (input("enter outfile: ") + ".json")
    horsefile = open(filename, 'w')
    horsefile.write(json.dumps(horsedict))
    horsefile.close()

main()
