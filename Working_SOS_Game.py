import tkinter as tk
from tkinter import messagebox

# This creates the window for the GUI
window = tk.Tk()
window.title("Grid Manager")
window.geometry("900x500")
label = tk.Label(window, text='SOS Game', fg='black', font=('Arial, 12'))
label.grid(row=0, column=0, padx=5, pady=10)


gameRan = False

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
    return BoardEntry.get()


sizeConfirm = tk.Button(window, text="Create Board", bg='black', fg='white',
                        command=lambda: printingBoard(BoardEntry.get()) and gameRan())
sizeConfirm.grid(row=0, column=6, padx=5, pady=1)


# For getting text on screen when button is clicked
def printingBoard(x):
    # print = tk.Label(text=BoardEntry.get(), bg='blue', fg='white')
    # print.grid(row=3, column=2)

    # The i  and j are switched i = Columns and j= Rows, This is the Game Board.
    global mSpots
    mSpots = [[tk.Button(gameBoard, text=str(j + 1) + ',' + str(i + 1), font=("Halvetica", 7), height=3, width=6,
                         bg='#ECECEC', fg='black', command=lambda i=i, j=j: clicking(i, j, slotAvailibility) , ) for i in
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
        mSpots[y][x].config(text="S", fg='blue')
        slotAvailibility[y][x] = 1
        whoseTurn = False

    elif whoseTurn == False and slotAvailibility[y][x] == 0:
        mSpots[y][x].config(text="O", fg='red')
        slotAvailibility[y][x] = 2
        whoseTurn = True
    else:
        messagebox.showwarning("Invalid Input", "This Square has Spot Taken Choose Another One")


# Radio buttons for game type 
r1 = tk.Radiobutton(window, text="Simple Game", value= 50)
r2 = tk.Radiobutton(window, text="General Game", value='General Game')
r1.grid(row=0, column=1, padx=5, pady=10)
r2.grid(row=0, column=2, padx=5, pady=10)

# Player Choice for S or O
p1Frame = tk.Frame();
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

window.mainloop()
