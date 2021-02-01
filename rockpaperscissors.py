import random
import json
import os


#globals
with open('data.json') as json_file:        #loads data.json which has what hands are possible and how they fair against other hands
        data = json.load(json_file)
winningStreak = 0 

def aiSelection():                          #returns a random handsign data set that contains the following attributes: id, name, winsAgainst, losesAgainst, tiesAgainst.
    numberOfOptions = 0
    for x in data["gangsigns"]:
        numberOfOptions +=1
    aiSelectedIndex = random.randint(1,numberOfOptions) - 1
    randomSelection = data["gangsigns"][aiSelectedIndex]
    return(randomSelection)


def humanSelection(userSelection):         ##returns the handsign data set for the handsign the user threw. If it returns -1 then something went wrong
    humanSelection = -1
    for x in data["gangsigns"]:
        if userSelection in x['name']:
            humanSelection = x
            break
    return(humanSelection)


def compareResults(aiData, userData):       # works out which hand wins between ai and user. Also returns a tie. -1 means something went wrong
    if userData['id'] in aiData['winsAgainst']:
        winner = 'ai'
    elif userData['id'] in aiData['losesAgainst']:
        winner = 'user'
    elif userData['id'] in aiData['tiesAgainst']:
        winner = 'tie'
    else:
        winner = -1
    return(winner)



def main():         
    global winningStreak                    #initialize some variables
    validSelection = False
    print("Welcome to rock paper scissors.")
    
    # gangsign = input().lower()

    while validSelection == False:          #Gets the user to throw a gang sign
        print("Would you like to throw 'rock', 'paper', or 'scissors'")
        gangsign = input()
        userData = humanSelection(gangsign) # Gets the data for the hand sign
        if userData != -1:
            validSelection = True
    randomSelection = aiSelection()         # selects a random handsign for the ai
    winner = compareResults (randomSelection, userData)

    print("You threw {}. The robot overlords threw {}".format(userData['name'],randomSelection['name']))

    if winner == 'user':
        winningStreak += 1
        print("Congrats on your win, your current winning streak is:", winningStreak)
    elif winner == 'ai':
        winningStreak = 0
        print("Big oof, the robot overlords have won this game")
    elif winner == 'tie':
        print("It is a tie! This does not affect your winning streak which is still:", winningStreak)
    elif winner == -1:
        print("Whoops, captain messed something up.")

    print("Would you like to play again? y/n")
    playAgain = input()
    if playAgain == 'y':
        main()
main()