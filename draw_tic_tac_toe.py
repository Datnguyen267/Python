"""
- The Goal: Tic Tac Toe draw
- Author: Dat Nguyen
- Create date: 2018-03-05
"""

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

test = [
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]
        ]
is_end = False
while is_end != True:
  player_1 = input("Your turn Player_1. ")
  process_input(player_1, test, 1)
  player_2 = input("Your turn Player_2. ")
  process_input(player_2, test, 2)
  print(draw_tic_tac_toe(test))

