# _____________
# | 0 | 1 | 2 |
# _____________
# | 3 | 4 | 5 |
# _____________
# | 6 | 7 | 8 |
# _____________
#
# X --> 1
# O --> -1
# empty place --> -
#

from random import randint


winning_sequences = [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8],
                     [0, 3, 6],
                     [1, 4, 7],
                     [2, 5, 8],
                     [0, 4, 8],
                     [2, 4, 6]]


def is_game_won(board, token):
    for winning_sequence in winning_sequences:
        if board[winning_sequence[0]] == token \
                and board[winning_sequence[1]] == token \
                and board[winning_sequence[2]] == token:
            return True
    return False


def is_game_drawn(board):
    if n_tokens_on_board(board) == 9 \
            and not is_game_won(board, 1)\
            and not is_game_won(board, -1):
        return False
    return True


def is_game_over(board):
    return is_game_won(board, 1) or is_game_won(board, -1) or not is_game_drawn(board)


def create_empty_board():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0]


def sub_board_from_board(board1, board2):
    if len(board1) is not len(board2):
        raise Exception('length of board1 is not equal to board2')
    sub_list = []

    # each element is subtracted
    for i in range(len(board1)):
        new_element = board2[i] - board1[i]
        sub_list.append(new_element)
    return sub_list


def contains_one(board, token):
    counter = 0
    for place in board:
        if place is token:
            counter += 1
    return counter == 1


def state_all_null_except_one(state):
    counter = 0
    for i in range(len(state)):
        if state[i] == -1 or state[i] == 1:
            counter += 1
    return counter == 1


def n_tokens_on_board(board):
    n_tokens = 0
    for token in board:
        if token == 1 or token == -1:
            n_tokens += 1
    return n_tokens


def empty_places_on_board(board):
    empty_places_on_b = []
    for i in range(9):
        if board[i] == 0:
            empty_places_on_b.append(i)
    return empty_places_on_b


def place_token_on_board(board, place, token):
    if board[place] == 1 or board[place] == -1:
        error = '{} is already occupied with {}'.format(place, token)
        raise Exception(error)
    else:
        board[place] = token
    return board


def get_next_random_place(board):
    empty_places_on_b = empty_places_on_board(board)
    random_number = randint(0, len(empty_places_on_b) - 1)
    return empty_places_on_b[random_number]


def get_next_random_state(board, token):
    new_board = list(board)
    next_random_place = get_next_random_place(board)
    new_board[next_random_place] = token
    return create_state_from_board(new_board, [0.5])


def create_state_from_board(board, value):
    new_state = [[], []]
    new_state[0] = board
    new_state[1] = value
    return new_state


def state_value(state):
    return state[1][0]


def place_to_get_to_state(board, next_game_state, token):
    subtracted_list = sub_board_from_board(next_game_state[0], board)
    for i in range(len(subtracted_list)):
        if subtracted_list[i] == -token:
            return i
    return 'place to get to next state was not found. board={}, next_game_state={}, token={}'.format(board, next_game_state, token)


def update_game_state_value(game_state, game_state_value):
    game_state[0][1] = game_state_value
    return game_state

