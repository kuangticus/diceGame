
class Player:
    def __init__(self, playerNum, name, scoreBoard ):
        self.__playerNum = playerNum
        self.__name = name
        self.__scoreBoard = scoreBoard
    
    def getScore(self):
        return self.__scoreBoard
    def getName(self):
        return self.__name

    def changeName(self, name):
        self.__name = name

    def addScore(self, num):
        self.__scoreBoard.append(num)
    # def rollDice ():

    
# initialize function that gets the player names and their position.
# Return: the array that has the names and indexes
def Players():
    numPlayers = input("How many players are there? ")
    playerNames = []
    numPlayers = int(numPlayers)
    for i in range(int(numPlayers)):
        name = input(f"Player {int(i+1)} Name: ")
        playerNames.append([i, name])
    return playerNames

def main ():

    players = Players()
    numPlayers = len(players)

    print(players)
    print(numPlayers)

    playerList = []
    for player in players:
        playerList.append(Player(player[0], player[1], []))

main()