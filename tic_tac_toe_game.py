"""
- The Goal: Tic Tac Toe game
- Author: Dat Nguyen
- Create date: 2018-03-13
"""

def draw_game_board(size):
  result = ''
  for i in range((int(size) * 2) + 1):
    if i % 2 == 0:
      for j in range(int(size)):
        result += ' ---'
    else:
      for j in range(int(size) + 1):
        result += '|   '
    result += '\n'
  return result


def draw_tic_tac_toe(game_board):
  size = len(game_board[0])
  result = ''
  for i in range((int(size) * 2) + 1):
    if i % 2 == 0:
      for j in range(int(size)):
        result += ' ---'
    else:
      for j in range(int(size) + 1):
        if j != size and (game_board[i // 2][j] != 0):
          if game_board[i // 2][j] == 1:
            mask = 'X'
          else:
            mask = 'O'
          result += '| ' + mask + ' '
        else:
          result += '|   '
    result += '\n'
  return result

def process_input(text, board, player):
  split_text = text.split(", ")
  result = board
  result[int(split_text[0])][int(split_text[1])] = player
  return result


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



game_board = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
  ]

print("Let's play tic tac toe!")
print(draw_game_board(3))

while True:
  player_1 = input("Your turn Player_1. ")
  game_board = process_input(player_1, game_board, 1)
  print(draw_tic_tac_toe(game_board))
  check = check_tic_tac_toe(game_board)
  if check == 1:
    print("Player_1 win.")
    break
  player_2 = input("Your turn Player_2. ")
  game_board = process_input(player_2, game_board, 2)
  print(draw_tic_tac_toe(game_board))
  is_end = check_tic_tac_toe(game_board)
  if check == 2:
    print("Player_2 win.")
    break
