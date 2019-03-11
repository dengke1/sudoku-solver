nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def check_column(board, x, y):
   '''
   checks column given x, y returns set of possible values for position
   empty set is returned if position is filled
   '''
   available_val = nums.copy()
   if board[y][x] != 0:
      return set()   
   for i in range (0, 9):
      if board[i][x] in nums:
         available_val.remove(board[i][x])

   return available_val

def check_row(board, x, y):
   '''
   checks row given x, y returns set of possible values for position
   empty set is returned if position is filled
   '''
   available_val = nums.copy()
   if board[y][x] != 0:
      return set()   
   for i in range (0, 9):
      if board[y][i] in nums:
         available_val.remove(board[y][i])
   
   return available_val

def check_quadrant(board, x, y):
   '''
   checks the 3x3 quadrant, returns set of possible values for position
   empty set is returned if position is filled
   '''
   # set min and max values for quadrant
   available_val = nums.copy()
   if board[y][x] != 0:
      return set()   
   
   minx = x//3*3
   miny = y//3*3
      
   for i in range(miny, miny+3):
      for j in range(minx, minx+3):
         if board[i][j] in nums:
            available_val.remove(board[i][j])
   
   return available_val
            
def triple_intersection(set1, set2, set3):
   return set1.intersection(set2).intersection(set3)

def next_loc(board):
   '''
   returns next location to fill in, along with set of available values
   -1 -1 set() is returned if board is full (ie complete)
   '''
   fewest = 9
   available_vals = set()
   x = -1; y = -1
   for i in range(0, 9): # y
      for j in range(0, 9): # x
         # skip over filled spaces
         if board[i][j] == 0:
            
            temp = triple_intersection(check_row(board, j, i),
                                       check_column(board, j, i),
                                       check_quadrant(board, j, i))         
            cur = len(temp)
            # finds space with fewest possible values
            if (cur < fewest):
               fewest = cur
               x = j; y = i
               available_vals = temp
            if cur == 1:
               return x, y, available_vals
   return x, y, available_vals

def print_board(board):
   ret = ""
   for i in range(0, 9):
      for j in range(0, 9):
         ret = ret + str(board[i][j]) + " " 
      ret +="\n"
   print(ret)

def solve(board):
   '''
   recursively solves sudoku
   '''
   nx, ny, ns = next_loc(board)
   # board is filled
   if nx == -1:
      return True
   for i in ns:
      board[ny][nx] = i
      if solve(board):
         return True
   # backtrack step
   board[ny][nx] = 0
      
   return False


if __name__ == "__main__":
   import os, sys, getopt
   while(1):
      puzzle = [[] for i in range(9)]
      file_name = input("Input file name (or q to quit): ")
      
      if (file_name == "q") or (file_name == "quit"):
         break
      
      try:
         f = open(file_name + ".txt", "r")
         puzzle_str = f.read()
         puzzle_str = puzzle_str.replace("\n", "").replace(" ", "")
         
         count = 0
         for i in range(0, 9):
            for j in range(0, 9):
               puzzle[i].append(int(puzzle_str[count]))
               count += 1
               
         solve(puzzle)
         print_board(puzzle)  
         f.close()         
          
      except:
         print("FILE DOES NOT EXIST TRY AGAIN")
         
         
 
   
   #puzzle = [[0, 8, 0,  0, 1, 0,  6, 0, 2], 
             #[0, 0, 0,  0, 0, 0,  1, 7, 9], 
             #[0, 0, 0,  9, 0, 7,  0, 8, 4], 
             
             #[0, 0, 0,  0, 4, 0,  2, 1, 7], 
             #[4, 7, 0,  3, 0, 2,  8, 0, 0], 
             #[0, 0, 8,  0, 9, 1,  4, 0, 3],
             
             #[0, 0, 2,  0, 3, 6,  9, 0, 8], 
             #[8, 6, 0,  5, 7, 0,  3, 2, 0], 
             #[0, 3, 9,  8, 2, 4,  0, 6, 5]]

   #puzzle = [[2, 0, 0,  9, 0, 0,  0, 0, 0], 
             #[0, 6, 0,  0, 0, 0,  0, 7, 0], 
             #[0, 0, 0,  5, 0, 0,  0, 0, 0], 
             
             #[0, 0, 0,  0, 6, 0,  0, 1, 0], 
             #[0, 0, 9,  8, 0, 0,  0, 0, 4], 
             #[0, 0, 5,  0, 0, 0,  0, 0, 0],
             
             #[0, 0, 0,  0, 0, 0,  0, 3, 5], 
             #[0, 0, 0,  0, 0, 0,  8, 0, 9], 
             #[4, 0, 0,  0, 7, 0,  0, 0, 0]]
