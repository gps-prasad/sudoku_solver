def is_valid_input(board,x,y,k):
    for i in range(9):
        if i!=y and board[x][i]==k:
            return False
        if i!=x and board[i][y]==k:
            return False
    
    for i in range((x//3)*3,(x//3)*3+3):
        for j in range((y//3)*3,(y//3)*3+3):
            if i!=x and j!=y and board[i][j]==k:
                return False
    return True

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j],end=' ')
        print()


def is_valid(board,x,y,k):
    for i in range(9):
        if board[x][i]==k:
            return False
        if board[i][y]==k:
            return False
    
    for i in range((x//3)*3,(x//3)*3+3):
        for j in range((y//3)*3,(y//3)*3+3):
            if board[i][j]==k:
                return False
    return True

def solveSudoku(board):
    
    
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                for k in range(1,10):
                    if is_valid(board,i,j,k):
                        board[i][j]=k
                        if solveSudoku(board):
                            return True
                        board[i][j]=0
                return False
    print_board(board)
    return True




board=  [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]

invalid=False
for i in range(9):
    for j in range(9):
        if board[i][j]!=0:
            if not is_valid_input(board,i,j,board[i][j]):
                print("Invalid Input")
                invalid=True
                break
    if invalid:
         break
if not invalid:      
    solveSudoku(board)
