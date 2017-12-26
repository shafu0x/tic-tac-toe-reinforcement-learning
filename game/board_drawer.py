# _____________
# | - | - | - |
# _____________
# | - | - | - |
# _____________
# | - | - | - |
# _____________

places = {'0': '-',
          '1': '-',
          '2': '-',
          '3': '-',
          '4': '-',
          '5': '-',
          '6': '-',
          '7': '-',
          '8': '-'}


def output_board():
    return '_____________\n| ' \
               + places['0'] \
               + ' | ' \
               + places['1'] \
               + ' | ' \
               + places['2'] \
               + ' |\n_____________\n| ' \
               + places['3'] \
               + ' | ' \
               + places['4'] \
               + ' | ' \
               + places['5'] \
               + ' |\n_____________\n| ' \
               + places['6'] \
               + ' | ' \
               + places['7'] \
               + ' | ' \
               + places['8'] \
               + ' |\n-------------'


def place_token_on_board(token, place):
    places[str(place)] = token


def display_board(board):
    for place in range(len(board)):
        if board[place] == 1:
            place_token_on_board('X', place)
        elif board[place] == -1:
            place_token_on_board('O', place)
        else:
            place_token_on_board('-', place)
    return output_board()





