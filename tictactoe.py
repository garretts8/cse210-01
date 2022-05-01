#Game Board
from tokenize import Number


board = [1,2,3,
         4,5,6,
         7,8,9]

#game is still in play
game_in_play = True

#To find who won the game or if there is a tie
winner = None

#current player playing
current_player = "X"
def main(): 
  play_game()  
#Display board
def display_board():
  print()
  print(board[0],board[1], board[2], sep= "|", flush=False)
  print('-+-+-')
  print(board[3],board[4], board[5], sep= "|", flush=False)
  print('-+-+-')
  print(board[6],board[7], board[8], sep= "|", flush=False)
  print()
  
#Play the game Tic Tac Toe
def play_game():
  #Display the board
  display_board()  
  #while the game is still in play
  while game_in_play:
    ##current player's turn
    handle_turn(current_player)
    #To check if the game has ended
    game_over_check()
    #switch to the next player
    switch_player()
  
#Current player's
def handle_turn(player):
  position = input(f"{player}'s turn to choose a square (1-9: ) ")
  position = int(position) - 1
  board[position] = player
  display_board()
  
def game_over_check():
    check_if_winner()
    check_if_tie(board)
    
def check_if_winner():
  global game_in_play
  global winner
  if (board[0] == board[1] == board[2] or
      board[3] == board[4] == board[5] or
      board[6] == board[7] == board[8] or
      board[0] == board[3] == board[6] or
      board[1] == board[4] == board[7] or
      board[2] == board[5] == board[8] or
      board[0] == board[4] == board[8] or
      board[2] == board[4] == board[6]):
    game_in_play = False
    print(f"{current_player} won")
  return

def check_if_tie(board):
  global game_in_play
  for box in range(9):
    if board[box] != "X" and board[box] != "O":
      return False
  game_in_play = False
  print("Tie Game")
  return 

def switch_player():
  #we needed to use the global vaiable to give current player a value
  global current_player
 # If the current player is "X" then change it to "O"
  if current_player  == "X":
    current_player = "O"
# If the current player is "O" then change it to "X"    
  elif current_player  == "O":
    current_player = "X"
  return

if __name__ == "__main__":
    main()
