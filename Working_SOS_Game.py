import tkinter as tk
from tkinter import messagebox

# This creates the window for the GUI
window = tk.Tk()
window.title("Grid Manager")
window.geometry("900x500")
label = tk.Label(window, text='SOS Game', fg='black', font=('Arial, 12'))
label.grid(row=0, column=0, padx=5, pady=10)

gameRan = False


def stopGame(x):
    messagebox.showinfo('Game Over',"A match has been made and "+ x +" has Won!")
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


def retBoardEntry():
    return int(BoardEntry.get())

# This variable to track  which game mode we are runing # True is Simple and False is General
gameType = tk.BooleanVar()
gameType.set(True)
# IDK
"""
def checksos(board):
    w = len(board[0])
    h = len(board)
    global firstHor
    firstHor = True

    # Check for horizontals.

    for row in board:
        s = ''.join([cell['text'] for cell in row])
        if 'SOS' in s:
            if firstHor == True:
                trackHor = 0
                firstHor = False
            trackHor = trackHor +1
            print("found horizontal sos")
            print(trackHor)
        elif 'SOSSOS'in s:
            trackHor = trackHor + 1
            print("found horizontal sos")
            print(trackHor)

    # Check for verticals.

    for col in range(w):
        s = ''.join([board[i][col]['text']for i in range(h)])
        if 'SOS' in s:

            print("found vertical sos")

    # Check for diagonals.  There are N-2 diagonals in each direction;
    # the outermost 2 are too short to hold SOS.

    for offset in range(0,w-2):
        # Start from the top and go SE.  If offset is 1, the
        # first string gets 1,0 then 2,1 then 3,2; the other
        # string gets 0,1 then 1,2 then 2,3.
        s1 = []
        s2 = []
        s3 = []
        s4 = []
        for i in range(0,w-offset):
            s1.append( board[i+offset][i]['text'] )
            s2.append( board[i][i+offset]['text'] )
            s3.append( board[i+offset][w-i-1]['text'] )
            s4.append( board[h-i-1][i+offset]['text'] )
        if 'SOS' in ''.join(s1) or 'SOS' in ''.join(s2) or \
           'SOS' in ''.join(s3) or 'SOS' in ''.join(s4):
            print("found diagonal sos")

board = []
for i in range(5):
    board.append( [{'text':' '} for _ in range(5)] )

board[1][1]['text'] = 'S'
board[1][2]['text'] = 'O'
board[1][3]['text'] = 'S'

board[1][4]['text'] = 'S'
board[2][4]['text'] = 'O'
board[3][4]['text'] = 'S'

board[2][2]['text'] = 'S'
board[3][3]['text'] = 'O'
board[4][4]['text'] = 'S'
"""


# IDK END


def checkAround(board, i, j):
    # Horizontal check
    if (i + 2) < retBoardEntry():
        if board[i + 1][j]['text'] == 'O' and board[i + 2][j]['text'] == 'S':
            if matchMade[i + 1][j] == 0 and matchMade[i+2][j] == 0:
                if whoseTurn == True:
                    board[i][j].config(bg='#FFBDBD')
                    board[i+1][j].config(bg='#FFBDBD')
                    board[i+2][j].config(bg='#FFBDBD')

                    matchMade[i][j] = 2
                    matchMade[i + 1][j] = 2
                    matchMade[i + 2][j] = 2
                    if gameType.get() == True:
                        stopGame("Player 2")



                else:
                    board[i][j].config(bg='#B2E4FF')
                    board[i+1][j].config(bg='#B2E4FF')
                    board[i+2][j].config(bg='#B2E4FF')

                    matchMade[i][j] = 1
                    matchMade[i+1][j] = 1
                    matchMade[i+2][j] = 1
                    if gameType.get() == True:
                        stopGame("Player 1")
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
                        stopGame("Player 2")
                else:
                    board[i][j].config(bg='#B2E4FF')
                    board[i][j + 1].config(bg='#B2E4FF')
                    board[i][j + 2].config(bg='#B2E4FF')

                    matchMade[i][j] = 1
                    matchMade[i][j+1] = 1
                    matchMade[i][j+2] = 1
                    if gameType.get() == True:
                        stopGame("Player 1")
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
                        stopGame("Player 2")


                else:
                    board[i][j].config(bg='#B2E4FF')
                    board[i + 1][j + 1].config(bg='#B2E4FF')
                    board[i + 2][j + 2].config(bg='#B2E4FF')

                    matchMade[i][j] = 1
                    matchMade[i+1][j + 1] = 1
                    matchMade[i+2][j + 2] = 1
                    if gameType.get() == True:
                        stopGame("Player 1")
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
                        stopGame("Player 2")



                else:
                    board[i][j].config(bg='#B2E4FF')
                    board[i + 1][j - 1].config(bg='#B2E4FF')
                    board[i + 2][j - 2].config(bg='#B2E4FF')

                    matchMade[i][j] = 1
                    matchMade[i + 1][j - 1] = 1
                    matchMade[i + 2][j - 2] = 1
                    if gameType.get() == True:
                        stopGame("Player 1")
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
def printingBoard(x):
    # print = tk.Label(text=BoardEntry.get(), bg='blue', fg='white')
    # print.grid(row=3, column=2)
    global matchMade
    matchMade = [[0 for xt in range(retBoardEntry())] for yt in range(retBoardEntry())]

    # The i  and j are switched i = Columns and j= Rows, This is the Game Board.
    global mSpots
    mSpots = [[tk.Button(gameBoard, text=str(j + 1) + ',' + str(i + 1), font=("Halvetica", 7), height=3, width=6,
                         bg='#ECECEC', fg='black', command=lambda i=i, j=j: clicking(i, j, slotAvailibility)) for i in
               range(int(BoardEntry.get()))] for j in range(int(BoardEntry.get()))]

    # this second Multi demensional array is going to be used to keep track whether the slot in the board is filled by anyone
    global slotAvailibility
    slotAvailibility = [[0 for xt in range(int(BoardEntry.get()))] for yt in range(int(BoardEntry.get()))]

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
def clicking(x, y, turnTrack):
    global whoseTurn

    # Keeps track of whose turn it is X is True O is False
    if slotAvailibility[y][x] == 0 and whoseTurn == True:
        mSpots[y][x].config(text='S', fg='blue')
        slotAvailibility[y][x] = 1
        whoseTurn = False

    elif whoseTurn == False and slotAvailibility[y][x] == 0:
        mSpots[y][x].config(text='O', fg='red')
        slotAvailibility[y][x] = 2
        whoseTurn = True
    else:
        messagebox.showwarning("Invalid Input", "This Square has Spot Taken Choose Another One")

    findSOS(mSpots)


# Radio buttons for game type 
r1 = tk.Radiobutton(window, text="Simple Game",variable=gameType,value= True)
r2 = tk.Radiobutton(window, text="General Game",variable=gameType, value= False)
r1.grid(row=0, column=1, padx=5, pady=10)
r2.grid(row=0, column=2, padx=5, pady=10)

# Player Choice for S or O
p1Frame = tk.Frame()
Player1Text = tk.Label(text="Player 1", fg='black', font=('Arial, 12'))
Player1Text.grid(row=4, column=0)
P1S = tk.Radiobutton(text="S", fg='blue', font=('Arial, 12'), value=2)
P1S.grid(row=5, column=0)
P1O = tk.Radiobutton(text="O", fg='blue', font=('Arial, 12'), value=1)
P1O.grid(row=6, column=0)

p2Frame = tk.Frame(master=window, width=100, height=100, bg="red")
Player2Text = tk.Label(text="Player 2", fg='black', font=('Arial, 12'))
Player2Text.grid(row=4, column=5)
P2S = tk.Radiobutton(text="S", fg='red', font='Arial, 12', value=1)
P2S.grid(row=5, column=5)
P2O = tk.Radiobutton(text="O", fg='red', font='Arial, 12', value=2)
P2O.grid(row=6, column=5)

class player:
    def __init__(self, x):
        self.icon = x

window.mainloop()
