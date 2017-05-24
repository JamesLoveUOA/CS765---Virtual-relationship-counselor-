import json

def main():
    advice_dict = build_advice_dict()
    horsemen_dict = readPhrases()
    
    horseman_result = initiate_agent(horsemen_dict)
    give_advice(horseman_result, advice_dict)

#reading the dictionary of the four horsemen
def readPhrases():
    filename = input("please enter filename: ")
    with open(filename+'.json', 'r') as f:
        try:
            data = json.load(f)
        # if the file is empty the ValueError will be thrown
        except ValueError:
            data = {}
    data = dict(data)
    print(data)
    return data

def build_advice_dict():
    #{0: Remember that all relationships, even healthy ones, have disagreements and conflicts, and while you might be feeling disatisfied with your relationship right now, I don't belive that your relationship exhibts any of the four horsemen.
    # 1: blahblah
    #}
    return []

#classify the text
#iterate through the dictionary of horsemen. return the horseman if it has a
#phrase that matches the sentence as substring
def classify_text(sentence):

    return 0

#find the highest horseman in the user list, and also their percentage
def classify_horseman(horsemen_list):
    freqDict = {0:0, 1:0, 2:0, 3:0, 4:0}

    #print (horsemen_list)
    for num in horsemen_list:
        if num == 0:
            freqDict[0] = freqDict[0] + 1
        elif num == 1:
            freqDict[1] = freqDict[1] + 1
        elif num == 2:
            freqDict[2] = freqDict[2] + 1
        elif num == 3:
            freqDict[3] = freqDict[3] + 1
        elif num == 4:
            freqDict[4] = freqDict[4] + 1

    horsemanResult = 0
    maxFreq = 0
    #print (freqDict)

    for horseman, freq in freqDict.items():
        if freq > maxFreq:
            maxFreq = freq
            horsemanResult = horseman

    length = len(horsemen_list)

    percentage = maxFreq/length

    #print(horsemanResult)
    #print(percentage)
    return [horsemanResult, percentage]
def get_sentences_for_horseman(userList, userHorsemen, horseman):
    result = []

    for i in range(0, len(userHorsemen)):
        if userHorsemen[i] == horseman:
            result.append(userList[i])

    #print(result)
    return result


def initiate_agent(horsemen_dict):
    #agent talks to user. "please enter your name and your partner's name" "ask for convo log"
<<<<<<< HEAD
    userName = input("Hi there, what's your name?")
    partnerName = input("Nice to meet you " + userName + ". What is your partner's name? ")
    convoFileName = input("Please enter the filename for the conversation log between you and " + partnerName + " you would like me to analyse. ")
    with open(convoFileName + '.txt', 'r') as f:
        convo = f.readlines()
        print(convo)
=======
    userName = input("Hi there, what's your name? ")
    partnerName = input("Nice to meet you " + userName + ". What is your partner's name? ")
    convoFileName = input("Please enter the filename for the conversation log between you and " + partnerName + " you would like me to analyse. ")
>>>>>>> Helen

    # initiate a list for each person based on user input
    userList = []
    partnerList = []

<<<<<<< HEAD

        #initiate a list for each person based on user input
=======
>>>>>>> Helen
    #read convo log and put each sentence into corresponding person's list (based on first character/word)
    with open(convoFileName + '.txt', 'r') as f:
        convo = f.readlines()
        for sentence in convo:
            name = sentence.split(":")[0]
            if (name == userName):
                userList.append(sentence.split(":")[1].strip())
            else:
                partnerList.append(sentence.split(":")[1].strip())


        #print(userList)
        #rint(partnerList)
        #print(convo)

    #initiate a list for each user, where each item corresponds to the horseman in that sentence at that index
    userHorsemen = []
    partnerHorsemen = []

    #go through each list and use classify_text() gets us a number for each phrase (number representing the horseman)
    for sentence in userList:
        userHorsemen.append(classify_text(sentence))

    for sentence in partnerList:
        partnerHorsemen.append(classify_text(sentence))

    #find the horseman with highest frequency and set that as the result for that person. also calculate the percentage
    userResult = classify_horseman(userHorsemen)
    partnerResult = classify_horseman(partnerHorsemen)

    userHorsemanSentence = get_sentences_for_horseman(userList, userHorsemen, userResult[0])
    partnerHorsemanSentence = get_sentences_for_horseman(partnerList, partnerHorsemen, partnerResult[0])

    userResult.append(userHorsemanSentence)
    partnerResult.append(partnerHorsemanSentence)
    print(userResult)
    print(partnerResult)
    #result: return a list of lists for each couple, and their horseman result, their percentage of that horseman,
    return (userResult, partnerResult)
    # ((int, float, []),("Name", int, float, [])]

#POTENTIALLY: we can ask more questions here
#use the advice dictionary and print out advices
def give_advice(result, advice_dict):
    return

main()
