# tic tac toe game
# main idea: user make a move -> verifies if he won -> if the user has won, end program, else -> another move by the other player
""" 
matrix : 0 | 1 | 2
         3 | 4 | 5
         6 | 7 | 8

    we'll have this type of verification: in the beginning, the matrix is full of "-"'s. 
    when mat[x][y] != "-", it's because it's already selected by one player. 

    player wins if:
    1. horizontal (1-2-3, 4-5-6, 7-8-9)
    2. vertical (1-4-7, 2-5-8, 3-6-9)
    3. diagonal (1-5-9, 3-5-7)

    otherwise if the table is full of X's or O's and there's no winner, (or without any -'s)?
    the game ends. it's a tie.
"""

def diag(matrix):
    center = matrix[1][1]
    if center == "-":
        return 0
    if matrix[0][0] == center == matrix[2][2] or matrix[0][2] == center == matrix[2][0]:
        return 1
    return 0

def hor(matrix):
    for n in range(len(matrix)):
        if matrix[n][0] != "-" and matrix[n][0] == matrix[n][1] == matrix[n][2]:
            return 1
    return 0

def ver(matrix):
    for n in range(len(matrix[0])):
        if matrix[0][n] != "-" and matrix[0][n] == matrix[1][n] == matrix[2][n]:
            return 1
    return 0

def ganhou(matrix):
    return diag(matrix) or hor(matrix) or ver(matrix)     

def tem_espaco(matrix):
    for lines in matrix:
        for item in lines:
            if item == '-':
                return 1
    return 0

def game(): 
    cont = 0
    mat = [['-' for _ in range(3)] for _ in range(3)]

    for lines in mat:
        print(' '.join(lines))
    print()

    while(not ganhou(mat) and tem_espaco(mat)):
        pos = int(input("insira uma posição (1-9): "))

        if pos <= 9 and pos >= 1:
            line = (pos - 1) // 3
            column = (pos-1) % 3

            if(mat[line][column] == "-"):
                if(cont % 2 == 0):
                    mat[line][column] = "X"
                else:
                    mat[line][column] = "O"
                cont += 1
            else:
                print("posição já ocupada. tente novamente ")
            
            for lines in mat:
                    print(' '.join(lines))
            print()
        else:
            print("posição inválida. tente novamente ")
            
    if ganhou(mat):
        if cont % 2 == 0:

            print("O jogador 2 venceu!")    
        else:
            print("O jogador 1 venceu!")
    else:
        print("Empate!")

game()