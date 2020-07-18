# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 08:13:11 2020

@author: cheerag.verma
"""


def solveSudokuHelper(row,col,n,board):
    
    num = board[row][col]
    
    #left
    j = col-1
    while j >=0:
        if board[row][j] == num:
            return False
        j-=1
        
    #right
    j = col+1
    while j < n:
        if board[row][j] == num:
            return False
        j+=1

    #up
    i = row -1
    while i <=n:
        if board[i][col] == num:
            return False
        i-=1
    
    #down
    i = row+1
    while i <=n:
        if board[i][col] == num:
            return False
        i+=1
        
    for row in range(row,row+3):
        for col in range(col,col+3):
            rowS=3*(i//3)
            colS=3*(j//3

    
    return True
    
    
    
def solveSudoku(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            ans = solveSudokuHelper(i,j,n,board) 
            if ans == False:
                return False
            
    else:
        return True
    
            
    

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')
    
    
# Python3 program to check whether 
# given sudoku board is valid or not 

# Checks whether there is any 
# duplicate in current row or not 
def notInRow(arr, row): 

	# Set to store characters seen so far. 
	st = set() 

	for i in range(0, 9): 

		# If already encountered before, 
		# return false 
		if arr[row][i] in st: 
			return False

		# If it is not an empty cell, insert value 
		# at the current cell in the set 
		if arr[row][i] != '.': 
			st.add(arr[row][i]) 
	
	return True

# Checks whether there is any 
# duplicate in current column or not. 
def notInCol(arr, col): 

	st = set() 

	for i in range(0, 9): 

		# If already encountered before, 
		# return false 
		if arr[i][col] in st: 
			return False

		# If it is not an empty cell, insert 
		# value at the current cell in the set 
		if arr[i][col] != '.': 
			st.add(arr[i][col]) 
	
	return True

# Checks whether there is any duplicate 
# in current 3x3 box or not. 
def notInBox(arr, startRow, startCol): 

	st = set() 

	for row in range(0, 3): 
		for col in range(0, 3): 
			curr = arr[row + startRow][col + startCol] 

			# If already encountered before, 
			# return false 
			if curr in st: 
				return False

			# If it is not an empty cell, 
			# insert value at current cell in set 
			if curr != '.': 
				st.add(curr) 
		
	return True

# Checks whether current row and current 
# column and current 3x3 box is valid or not 
def isValid(arr, row, col): 

	return (notInRow(arr, row) and notInCol(arr, col) and
			notInBox(arr, row - row % 3, col - col % 3)) 

def isValidConfig(arr, n): 

	for i in range(0, n): 
		for j in range(0, n): 

			# If current row or current column or 
			# current 3x3 box is not valid, return false 
			if not isValid(arr, i, j): 
				return False
		
	return True

# Drivers code 
if __name__ == "__main__": 

	board = [[ int(ele) for ele in input().split() ]for i in range(9)]
		
	if isValidConfig(board, 9): 
		print("Yes") 
	else: 
		print("NO") 

# This code is contributed by Rituraj Jain 

# Function to check if a given row is valid. It will return:
# -1 if the row contains an invalid value
# 0 if the row contains repeated values
# 1 is the row is valid.
def valid_row(row, grid):
  temp = grid[row]
  # Removing 0's.
  temp = list(filter(lambda a: a != 0, temp))
  # Checking for invalid values.
  if any(i < 0 and i > 9 for i in temp):
    print("Invalid value")
    return -1
  # Checking for repeated values.
  elif len(temp) != len(set(temp)):
    return 0
  else:
    return 1
# Function to check if a given column is valid. It will return:
# -1 if the column contains an invalid value
# 0 if the columncontains repeated values
# 1 is the column is valid.
def valid_col(col, grid):
  # Extracting the column.
  temp = [row[col] for row in grid]
  # Removing 0's. 
  temp = list(filter(lambda a: a != 0, temp))
  # Checking for invalid values.
  if any(i < 0 and i > 9 for i in temp):
    print("Invalid value")
    return -1
  # Checking for repeated values.
  elif len(temp) != len(set(temp)):
    return 0
  else:
    return 1
# Function to check if all the subsquares are valid. It will return:
# -1 if a subsquare contains an invalid value
# 0 if a subsquare contains repeated values
# 1 if the subsquares are valid.
def valid_subsquares(grid):
  for row in range(0, 9, 3):
      for col in range(0,9,3):
         temp = []
         for r in range(row,row+3):
            for c in range(col, col+3):
              if grid[r][c] != 0:
                temp.append(grid[r][c])
          # Checking for invalid values.
         if any(i < 0 and i > 9 for i in temp):
             print("Invalid value")
             return -1
         # Checking for repeated values.
         elif len(temp) != len(set(temp)):
             return 0
  return 1
# Function to check if the board invalid.
def valid_board(grid):
  # Check each row and column.
  for i in range(9):
      res1 = valid_row(i, grid)
      res2 = valid_col(i, grid)
      # If a row or column is invalid then the board is invalid.
      if (res1 < 1 or res2 < 1):
          print("The board is invalid")
          return
  # If the rows and columns are valid then check the subsquares.
  res3 = valid_subsquares(grid)
  if (res3 < 1):
      print("The board is invalid")
  else:
      print("The board is valid")
 
board = [[1, 4, 7, 0, 0, 0, 0, 0, 3],
        [2, 5, 0, 0, 0, 1, 0, 0, 0],
        [3, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 2, 0, 0, 0, 4],
        [0, 0, 0, 4, 1, 0, 0, 2, 0],
        [9, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 9],
        [4, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 0, 0, 8, 0, 0, 7]]

if (valid_board(board)):
    print("true")
else:
    print('false')