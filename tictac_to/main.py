#profiency test, tic tac toe, Maisha Tapia Paredes
import random

def print_board(ttt_board):
# function that prints the tic tac toe board
  print(f" {ttt_board[0]} | {ttt_board[1]} | {ttt_board[2]} ")
  print("---+---+---")
  print(f" {ttt_board[3]} | {ttt_board[4]} | {ttt_board[5]} ")
  print("---+---+---")
  print(f" {ttt_board[6]} | {ttt_board[7]} | {ttt_board[8]} ")

def check_win(ttt_board, player):
#Checks options for the user to win 
  winning_combinations = [[0, 1, 2],
                          [3, 4, 5],
                          [6, 7, 8],
                          [0, 3, 6],
                          [1, 4, 7],
                          [2, 5, 8],
                          [0, 4, 8],
                          [2, 4, 6]]
  for combo in winning_combinations:
      if ttt_board[combo[0]] == ttt_board[combo[1]] == ttt_board[combo[2]] == player:
          return True
  return False

def computer(ttt_board):
#computers move randomly
  empty_spaces = [i for i in range(9) if ttt_board[i] == " "]
  return random.choice(empty_spaces)

def play_game():
  print('This is a Tic tac toe game! It is just like a normal game of Tic tac toe the difference is\ninstead of writing the X you would type in a number (0-8) to\nplace the X left to right and so on \nthis is for each of the rows.')
#This function asks the questions and puts the spots into the board
  ttt_board = [" " for _ in range(9)]
  current_player = "X"

  while True:
      print_board(ttt_board)
      print(f"Player {current_player}'s turn.")

      if current_player == "X":
          while True:
              move = int(input("Enter your move (0-8): "))
              if 0 <= move <= 8 and ttt_board[move] == " ":
                  ttt_board[move] = current_player
                  break
              else:
                  print("Invalid move. Try again.")
      else:
          move = computer(ttt_board)
          ttt_board[move] = current_player
          print(f"Computer's move: {move + 1}")

      if check_win(ttt_board, current_player):
          print_board(ttt_board)
          print(f"Player {current_player} wins!")
          break

      if " " not in ttt_board:
          print_board(ttt_board)
          print("It's a tie!")
          break

      current_player = "O" if current_player == "X" else "X"

#this uses a specific name the computer knows to start the program at the play_game function
if __name__ == "__main__":
   play_game()