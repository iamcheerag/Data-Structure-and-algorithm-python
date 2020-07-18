# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 07:53:42 2020

@author: cheerag.verma
"""

"""
N-Queens

You are given N, and for a given N x N chessboard, find a way to place N queens such that no queen can attack any other queen on the chess board. A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens. You have to print all such configurations.
Input Format :
    Line 1 : Integer N
    Output Format :
    One Line for every board configuration. 
    Every line will have N*N board elements printed row wise and are separated by space
    Note : Don't print anything if there isn't any valid configuration.
    Constraints :
    1<=N<=10
    Sample Input 1:
    4
    Sample Output 1 :
    0 1 0 0 0 0 0 1 1 0 0 0 0 0 1 0 
    0 0 1 0 1 0 0 0 0 0 0 1 0 1 0 0
"""

def isSafe(row,col,board):
    
    """
    We don't need to check for the left and right position ,because we are placing only 1 queen in the same row'
    """
    
    
    #checking vertically in the same col
    i = row - 1
    while i>=0:
        if board[i][col] == 1:
            return False
        i-=1


    #left diagonal
    i = row-1 
    j = col-1
    while i >= 0 and j >=0:
        if board[i][j] == 1:
            return False
        i-=1
        j-=1
        
        
    #right diagonal
    i = row-1
    j = col+1
    while i>=0 and j <n:
        if board[i][j] == 1:
            return False
        i-=1
        j+=1
        
    return True # IF ALL THE ABOVE CONDITIONS ARE SATISFYIED THEN QUEEN IS NOT IN DANGER
        
        

def nQueensHelper(row,n,board):
    #base case
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
            
        print()
        
    for col in range(n):
    
        if isSafe(row,col,board) == True:  #checking all the condition before placing queen.
            board[row][col] = 1
            nQueensHelper(row+1, n, board)
            board[row][col] = 0
            
    return 


def nQueens(n):
    #board creation
    board = [[0 for j in range(n)]for i in range(n)]
    nQueensHelper(0,n,board)
    
    
n = int(input())
nQueens(n)