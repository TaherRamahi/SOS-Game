from  Working_SOS_Game import *

def checkAround(board, i, j):
    #Horizontal check
    if board[i+1][j] == 'O'and board[i+2][j] == 'S':
        return 'Its a Match Horizontally'
    elif board[i][j+1] == 'O' and board[i][j+2] == 'S':
        return 'Its a Match vertically'

def findSOS(board):
    # horizontal
    for i in range(BoardEntry):
        for j in range(BoardEntry):
            if board[i][j].text == 'S':
                checkAround(board, i, j)
