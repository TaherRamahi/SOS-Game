import tkinter as tk
from tkinter import messagebox
from math import *
import random
# This creates the window for the GUI
window = tk.Tk()
window.title("Grid Manager")
window.geometry("900x500")
label = tk.Label(window, text='SOS Game', fg='black', font=('Arial, 12'))
label.grid(row=0, column=0, padx=5, pady=10)

class player:
    playerGamePeice = ''
    # This Variable below is to track if we are working with a Computer or Human
    isThisCom = False
    def __init__(self, x, playerSelection):
        self.playerScore = x
        self.playerGamePeice = playerSelection
    def updatingPlayerSelection(self, x):
        self.playerGamePeice = x
    def printAi(self, whoseTurn):
            pass


player1 = player(0, 'S')
player2 = player(0,'O')


# This Class is for Computer Moves will be making a simple and a complex version
class comAI:
    playerGamePeice = ''
    # This Variable below is to track if we are working with a Computer or Human
    isThisCom = True
    def __init__(self, playerNum):
        # Assigning which player we are True player 1 and False is player 2
        whichPlayer = playerNum



    def rowReturner(self):
        rowComputer = random.randint(1, retBoardEntry())
        print ('////////////////////////////////')
        print (str(rowComputer -1))
        return rowComputer - 1

    def columnReturner(self):
        columnComputer = random.randint(1, retBoardEntry())
        print('////////////////////////////////')
        print(str(columnComputer - 1))
        return columnComputer - 1
    def printAi(self, whoseTurn):

        i = self.rowReturner()
        j = self.columnReturner()
        tempTurnTrack = whoseTurn
        print('Row '+str(i)+' Col ' + str(j))
        tempList = [i,j]
        if slotAvailibility[i][j] == 0:
            return tempList

        else:
            self.printAi(whoseTurn)


# Setting up playerSelection on bored
var1 = tk.IntVar()
var2 = tk.IntVar()
var1.set(0)
var2.set(1)

# UPDATE IN PROGRESS (TRYING TO SET THE ENTITIES AND THERE LOGOS)
def settingTheEntities(optionSelected, whichOfPlayers):
    if whichOfPlayers == 1:
        global player1
        if optionSelected == 0:
            player1 .playerGamePeice = 'S'
        elif  optionSelected == 1:
            player1.playerGamePeice = 'O'
        else:
            player1 = comAI(1)

    elif whichOfPlayers == 2:
        global player2
        if optionSelected == 0:
            player2.playerGamePeice = 'S'
        elif  optionSelected == 1:
            player2.playerGamePeice = 'O'
        else:
            player2 = comAI(2)


def setPlayerSelection( playerSelection, whichPlayer):
    if whichPlayer == 1:
        player1.selection = var1.get()
    elif whichPlayer == 2:
        player2.selection = var2.get()

    print('we got inside of the alteration')

p1Frame = tk.Frame()
Player1Text = tk.Label(text="Player 1", fg='black', font=('Arial, 12'))
Player1Text.grid(row=4, column=0)
P1S = tk.Radiobutton(text="S", fg='blue', font=('Arial, 12'),variable= var1, value=0 ,command= lambda:[settingTheEntities(0, 1),setPlayerSelection(0, 1)])
P1S.grid(row=5, column=0)
P1O = tk.Radiobutton(text="O", fg='blue', font=('Arial, 12'),variable= var1 ,value=1 ,command= lambda:[settingTheEntities(1, 1),setPlayerSelection(1, 1)])
P1O.grid(row=6, column=0)
P1C = tk.Radiobutton(text="Computer", fg='blue', font=('Arial, 12'),variable= var1 ,value=2,command= lambda:[settingTheEntities(2, 1),setPlayerSelection(2, 1)])
P1C.grid(row=7, column=0)


p2Frame = tk.Frame(master=window, width=100, height=100, bg="red")
Player2Text = tk.Label(text="Player 2", fg='black', font=('Arial, 12'))
Player2Text.grid(row=4, column=5)
P2S = tk.Radiobutton(text="S", fg='red', font='Arial, 12',variable= var2, value=0 , command= lambda: [settingTheEntities(0, 2),setPlayerSelection(0, 2)])
P2S.grid(row=5, column=5)
P2O = tk.Radiobutton(text="O", fg='red', font='Arial, 12',variable= var2, value=1, command= lambda:[settingTheEntities(1, 2),setPlayerSelection(1, 2)])
P2O.grid(row=6, column=5)
P2C = tk.Radiobutton(text="Computer", fg='red', font=('Arial, 12'),variable= var2, value=2, command= lambda:[settingTheEntities(2, 2),setPlayerSelection(2, 2)])
P2C.grid(row=7, column=5)
# End Player Selection

gameRan = False

firstRunGenGameStop = tk.BooleanVar()
firstRunGenGameStop.set(True)




#This function to be called when simple game is ready to be terminated
def simpleStopGame(x):
    messagebox.showinfo('Game Over', "A match has been made and " + x + " has Won!")
    window.destroy()
def generalStopGame():
    print("We are in the Gen Stop Game")

    global trackIfFull
    trackIfFull = 0

    for i in range(retBoardEntry()):
        for j in range(retBoardEntry()):
            if slotAvailibility[i][j] == 1 or slotAvailibility[i][j] == 2:
                trackIfFull = trackIfFull + 1
                print(trackIfFull)

    firstRunGenGameStop.set(False)

    if trackIfFull == pow(int(len(slotAvailibility)), 2):
        print("WE Got to the general stop")

        if player1.playerScore > player2.playerScore:
            messagebox.showinfo('Game Over', "The Bored is Full and Player 1 has Won!")
            window.destroy()

        elif player1.playerScore < player2.playerScore:
            messagebox.showinfo('Game Over', "The Bored is Full and Player 2 has Won!")
            window.destroy()
        else:
            messagebox.showinfo('Game Over', "It is a tie")
            window.destroy()


def checkGameRan():
    gameRan = True


# Createing Board in Frame Widget, this will be used in order to insure that all game board peices stay together.
gameBoard = tk.LabelFrame(window, text="Game Board")
gameBoard.grid(row=3, column=3)

# Board size aquiring
BSizeText = tk.Label(text="Enter Desired Board Size", fg='black', font=('Arial, 12'))
BSizeText.grid(row=0, column=4, padx=5, pady=10)

BoardEntry = tk.Entry(fg="black", bg="white", width=1)
BoardEntry.grid(row=0, column=5, padx=5, pady=10)

global firstTime
firstTime = 0


def retBoardEntry():
    return int(BoardEntry.get())


# This variable to track which game mode we are runing # True is Simple and False is General
gameType = tk.BooleanVar()
gameType.set(True)

# This is the Algorythm to check if we have an SOS
def checkAround(board, i, j):
    print("This is player 1 selection ", player1.playerGamePeice)
    print("This is player 2 selection ", player2.playerGamePeice)
    # Horizontal check
    if (i + 2) < retBoardEntry():
        if board[i + 1][j]['text'] == 'O' and board[i + 2][j]['text'] == 'S':
            if matchMade[i + 1][j] == 0 and matchMade[i + 2][j] == 0:
                if whoseTurn == True:
                    board[i][j].config(bg='#FFBDBD')
                    board[i + 1][j].config(bg='#FFBDBD')
                    board[i + 2][j].config(bg='#FFBDBD')

                    matchMade[i][j] = 2
                    matchMade[i + 1][j] = 2
                    matchMade[i + 2][j] = 2
                    if gameType.get() == True:
                        simpleStopGame("Player 2")
                    else:
                        player2.playerScore = player2.playerScore + 1
                        generalStopGame()


                else:
                    board[i][j].config(bg='#B2E4FF')
                    board[i + 1][j].config(bg='#B2E4FF')
                    board[i + 2][j].config(bg='#B2E4FF')

                    matchMade[i][j] = 1
                    matchMade[i + 1][j] = 1
                    matchMade[i + 2][j] = 1
                    if gameType.get() == True:
                        simpleStopGame("Player 1")
                    else:
                        player1.playerScore = player1.playerScore + 1
                        generalStopGame()
                print('Its a Match verticaly')
        # vertcal check
    if (j + 2) < retBoardEntry():
        if board[i][j + 1]['text'] == 'O' and board[i][j + 2]['text'] == 'S':
            if matchMade[i][j + 1] == 0 and matchMade[i][j + 2] == 0:

                if whoseTurn == True:
                    board[i][j].config(bg='#FFBDBD')
                    board[i][j + 1].config(bg='#FFBDBD')
                    board[i][j + 2].config(bg='#FFBDBD')
                    matchMade[i][j] = 2
                    matchMade[i][j + 1] = 2
                    matchMade[i][j + 2] = 2
                    if gameType.get() == True:
                        simpleStopGame("Player 2")
                    else:
                        player2.playerScore = player2.playerScore + 1
                        generalStopGame()

                else:
                    board[i][j].config(bg='#B2E4FF')
                    board[i][j + 1].config(bg='#B2E4FF')
                    board[i][j + 2].config(bg='#B2E4FF')

                    matchMade[i][j] = 1
                    matchMade[i][j + 1] = 1
                    matchMade[i][j + 2] = 1
                    if gameType.get() == True:
                        simpleStopGame("Player 1")
                    else:
                        player1.playerScore = player1.playerScore + 1
                        generalStopGame()
                print('Its a Match horizontaly')
    if (i + 2) < retBoardEntry() and (j + 2) < retBoardEntry():
        if board[i + 1][j + 1]['text'] == 'O' and board[i + 2][j + 2]['text'] == 'S':
            if matchMade[i + 1][j + 1] == 0 and matchMade[i + 2][j + 2] == 0:
                if whoseTurn == True:
                    board[i][j].config(bg='#FFBDBD')
                    board[i + 1][j + 1].config(bg='#FFBDBD')
                    board[i + 2][j + 2].config(bg='#FFBDBD')

                    matchMade[i][j] = 2
                    matchMade[i + 1][j + 1] = 2
                    matchMade[i + 2][j + 2] = 2
                    if gameType.get() == True:
                        simpleStopGame("Player 2")
                    else:
                        player2.playerScore = player2.playerScore + 1
                        generalStopGame()


                else:
                    board[i][j].config(bg='#B2E4FF')
                    board[i + 1][j + 1].config(bg='#B2E4FF')
                    board[i + 2][j + 2].config(bg='#B2E4FF')

                    matchMade[i][j] = 1
                    matchMade[i + 1][j + 1] = 1
                    matchMade[i + 2][j + 2] = 1
                    if gameType.get() == True:
                        simpleStopGame("Player 1")
                    else:
                        player1.playerScore = player1.playerScore + 1
                        generalStopGame()
                print('Its a match Diagnally right')
    if (i + 2) < retBoardEntry() and (j - 2) > -1:
        if board[i + 1][j - 1]['text'] == 'O' and board[i + 2][j - 2]['text'] == 'S':
            if matchMade[i + 1][j - 1] == 0 and matchMade[i + 2][j - 2] == 0:
                if whoseTurn == True:
                    board[i][j].config(bg='#FFBDBD')
                    board[i + 1][j - 1].config(bg='#FFBDBD')
                    board[i + 2][j - 2].config(bg='#FFBDBD')

                    matchMade[i][j] = 2
                    matchMade[i + 1][j - 1] = 2
                    matchMade[i + 2][j - 2] = 2
                    if gameType.get() == True:
                        simpleStopGame("Player 2")
                    else:
                        player2.playerScore = player2.playerScore + 1
                        generalStopGame()



                else:
                    board[i][j].config(bg='#B2E4FF')
                    board[i + 1][j - 1].config(bg='#B2E4FF')
                    board[i + 2][j - 2].config(bg='#B2E4FF')

                    matchMade[i][j] = 1
                    matchMade[i + 1][j - 1] = 1
                    matchMade[i + 2][j - 2] = 1
                    if gameType.get() == True:
                        simpleStopGame("Player 1")
                    else:
                        player1.playerScore = player1.playerScore + 1
                        generalStopGame()

            print('Its a match Diagnally left')


# The i and j I belive are switched the order rn is coloumn then row [TESTING REQUIRED]
def findSOS(board):
    # horizontal
    for i in range(int(BoardEntry.get())):
        for j in range(int(BoardEntry.get())):
            if board[i][j]['text'] == 'S':
                checkAround(board, i, j)


sizeConfirm = tk.Button(window, text="Create Board", bg='black', fg='white',
                        command=lambda: printingBoard(BoardEntry.get()) and gameRan())
sizeConfirm.grid(row=0, column=6, padx=5, pady=1)


# For getting text on screen when button is clicked
# this second Multi demensional array is going to be used to keep track whether the slot in the board is filled by anyone

def printingBoard(x):
    # print = tk.Label(text=BoardEntry.get(), bg='blue', fg='white')
    # print.grid(row=3, column=2)
    global matchMade
    matchMade = [[0 for xt in range(int(BoardEntry.get()))] for yt in range(int(BoardEntry.get()))]

    # The i  and j are switched i = Columns and j= Rows, This is the Game Board.
    global mSpots

    mSpots = [[tk.Button(gameBoard, text=str(j + 1) + ',' + str(i + 1), font=("Halvetica", 7), height=3, width=6,
                         bg='#ECECEC', fg='black', command=lambda i=i, j=j: clicking(i, j)) for i in
               range(int(BoardEntry.get()))] for j in range(int(BoardEntry.get()))]

    global slotAvailibility
    slotAvailibility = [[0 for xt in range(retBoardEntry())] for yt in range(retBoardEntry())]

    test = tk.Label(text=len(mSpots))
    test.grid(row=6, column=3)

    # Prints the Game Board to the Screen
    for i in range(int(x)):
        for j in range(int(x)):
            mSpots[i][j].grid(row=i + 4, column=j + 4)
            pass


# This variable is used to keep track of whose turn it is X is True O is False
whoseTurn = True


# Passed the Rows and columns in the right order X is Rows and Y is Columns 
# This Functions is ment to dictate what happens when we click on of our squares
def clicking(x, y):
    global whoseTurn

    #This Set of If statments is ment to insure that the computer is a assigned the correct Variable
    if player1.isThisCom == False and player2.isThisCom == True:
        if player1.playerGamePeice == 'S':
            player2.playerGamePeice = 'O'
            print("Scenario" + "1")
            tempList = player2.printAi(whoseTurn)

        elif player1.playerGamePeice == 'O':
            player2.playerGamePeice = 'S'
            print("Scenario" + "2")
            tempList = player2.printAi(whoseTurn)

    elif player1.isThisCom == True and player2.isThisCom == False:
        if player2.playerGamePeice == 'S':
            player1.playerGamePeice = 'O'
            print("Scenario" + "3")
            tempList = player1.printAi(whoseTurn)

        elif player2.playerGamePeice == 'O':
            player1.playerGamePeice == 'S'
            print("Scenario" + "4")
            tempList = player1.printAi(whoseTurn)

    elif player1.isThisCom == True and player2.isThisCom == True:
        player1.playerGamePeice == 'S'
        player2.playerGamePeice == 'O'
        print("Scenario" + "5")
        tempList = player1.printAi(whoseTurn)

    # This Set of If statements is to allocate which square should be filled depending on is its a computer or not and for which player
    if slotAvailibility[y][x] == 0 and whoseTurn == True and player1.isThisCom == False:
        mSpots[y][x].config(text=player1.playerGamePeice, fg='blue')
        slotAvailibility[y][x] = 1
        whoseTurn = False

    elif whoseTurn == False and slotAvailibility[y][x] == 0 and player2.isThisCom == False:
         mSpots[y][x].config(text=player2.playerGamePeice, fg='red')
         slotAvailibility[y][x] = 2
         whoseTurn = True

    elif whoseTurn == True and player1.isThisCom == True:
        i = tempList[0]
        j = tempList[1]
        mSpots[tempList[0]][tempList[1]].config(text=player1.playerGamePeice, fg='blue')
        slotAvailibility[tempList[0]][tempList[1]] = 1
        whoseTurn = False

    elif whoseTurn == False and player2.isThisCom == True:
        i = tempList[0]
        j = tempList[1]
        mSpots[i][j].config(text=player2.playerGamePeice, fg='red')
        slotAvailibility[tempList[0]][tempList[1]] = 2
        whoseTurn = True

    else:
        messagebox.showwarning("Invalid Input", "This Square has Spot Taken Choose Another One")

    if player1.isThisCom== True and player2.isThisCom == True:
        clicking(x,y)
    print(slotAvailibility)
    findSOS(mSpots)


# Radio buttons for game type
r1 = tk.Radiobutton(window, text="Simple Game", variable=gameType, value=True)
r2 = tk.Radiobutton(window, text="General Game", variable=gameType, value=False)
r1.grid(row=0, column=1, padx=5, pady=10)
r2.grid(row=0, column=2, padx=5, pady=10)

# Player Choice for S or O

window.mainloop()
