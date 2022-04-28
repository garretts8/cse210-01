board = [1,2,3,4,5,6,7,8,9]
for i in board:
  print(i)
  
print()
print(f"{board[0]}|{board[1]}|{board[2]}")
print('-+-+-')
print(f"{board[3]}|{board[4]}|{board[5]}")
print('-+-+-')
print(f"{board[6]}|{board[7]}|{board[8]}")
print()

board = [1,2,3,4,5,6,7,8,9]
for i in board:
  print(i)
  
choosex = int(input("x's turn to choose a square (1-9: ) "))
board[choosex - 1] = "x"
print(board)
  
