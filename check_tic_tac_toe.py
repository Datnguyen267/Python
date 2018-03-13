"""
- The Goal: Check Tic Tac Toe
- Author: Dat Nguyen
- Create date: 2018-02-13
"""

def check_tic_tac_toe(game_board):
  # check rows
  for x in range(0, 3):
    row = set([game_board[x][0], game_board[x][1], game_board[x][2]])
    if len(row) == 1 and game_board[x][0] != 0:
      return game_board[x][0];

  # check columns
  for x in range(0, 3):
    row = set([game_board[0][x], game_board[1][x], game_board[2][x]])
    if len(row) == 1 and game_board[0][x] != 0:
      return game_board[0][x];

  # check diagonals
  for x in range(0, 3):
    diag1 = set([game_board[0][0], game_board[1][1], game_board[2][2]])
    diag2 = set([game_board[0][2], game_board[1][1], game_board[2][0]])
    if (len(diag1) == 1 or len(diag1) == 1) and game_board[1][1] != 0:
      return game_board[1][1];

  return 0

test = [
       [1, 2, 0],
       [2, 1, 0],
       [2, 1, 1]
        ]

print(check_tic_tac_toe(test))

