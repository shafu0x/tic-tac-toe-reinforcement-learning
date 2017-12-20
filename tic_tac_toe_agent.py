# _____________
# | 0 | 1 | 2 |
# _____________
# | 3 | 4 | 5 |
# _____________
# | 6 | 7 | 8 |
# _____________
#

from random import randint

from board_drawer import display_board, output_board

winning_state = [[[1, 1, 1, 0, 0, 0, 0, 0, 0], [1]],
                 [[0, 0, 0, 1, 1, 1, 0, 0, 0], [1]],
                 [[0, 0, 0, 0, 0, 0, 1, 1, 1], [1]],
                 [[1, 0, 0, 0, 1, 0, 0, 0, 1], [1]],
                 [[0, 0, 1, 0, 1, 0, 0, 0, 1], [1]],
                 [[1, 0, 0, 1, 0, 0, 1, 0, 0], [1]],
                 [[0, 1, 0, 0, 1, 0, 0, 1, 0], [1]],
                 [[0, 0, 1, 0, 0, 1, 0, 0, 1], [1]]]

winning_sequences = [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8],
                     [0, 3, 9],
                     [1, 4, 7],
                     [2, 5, 8],
                     [0, 4, 8],
                     [2, 4, 6]]


def is_game_won(board, token):

    for winning_sequence in winning_sequences:

        if (board[winning_sequence[0]] and board[winning_sequence[1]] and board[winning_sequence[2]]) is token:
            return True

    return False


def is_game_drawn(board):
    if get_n_of_tokens_on_board(board) < 9:
        return False
    if get_n_of_tokens_on_board(board) == 9:
        if not is_game_won(board, 1) and not is_game_won(board, -1):
            return False

    return True


def create_empty_board():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0]


def subtract_list_from_list(list1, list2):

    if len(list1) is not len(list2):
        raise Exception

    new_list = []

    for i in range(len(list1)):
        new_element = list2[i] - list1[i]
        new_list.append(new_element)

    return new_list


def get_n_of_tokens_on_board(board):

    counter = 0

    for token in board:
        if token == 1 or token == -1:
            counter += 1

    return counter


def get_empty_places_on_board(board):

    empty_places_on_board = []

    for i in range(9):
        if board[i] == 0:
            empty_places_on_board.append(i)

    return empty_places_on_board


def place_token_on_board(board, place, token):

    if board[place] == 1 or board[place] == -1:
        raise Exception
    else:
        board[place] = token
    return board


def get_next_random_play(board):

    empty_places_on_board = get_empty_places_on_board(board)

    random_number = randint(0, len(empty_places_on_board) - 1)

    return empty_places_on_board[random_number]


def get_next_random_state(board, token):
    next_random_place = get_next_random_play(board)
    board[next_random_place] = token

    return create_state_from_board(board, 0.5)


def create_new_board(board, place, token):
    new_board = board
    new_board[place] = token
    return new_board


def create_state_from_board(board, state_value):
    new_state = [[], []]

    new_state[0] = board
    new_state[1] = state_value
    return new_state


def get_value_of_game_state(state):
    return state[1][0]


def get_place_of_token_to_get_to_next_state(board, next_game_state, token):

    subtracted_list = subtract_list_from_list(next_game_state, board)

    for i in range(len(subtracted_list)):
        if subtracted_list[i] == -token:
            return i

    return -1


class Agent:

    def __init__(self):

        self.game_states = []
        self.previous_game_state_value = 0

    def set_game_states(self, states):
        self.game_states = states

    def add_game_state(self, game_state):

        if game_state not in self.game_states:
            self.game_states.append(game_state)

    def get_next_states(self, tokens_played, board):

        next_game_states = []

        for game_state in self.game_states:

            board = game_state[0]

            if get_n_of_tokens_on_board(board) == tokens_played + 1:
                next_game_states.append(game_state)

        return next_game_states

    def get_next_greedy_state(self, tokens_played, board):

        next_greedy_game_state = [[0], [0]]

        for game_state in self.get_next_states(tokens_played, board):
            if game_state[1] > next_greedy_game_state[1]:
                next_greedy_game_state = game_state

        return next_greedy_game_state[0]

    def display_game_states(self):

        print('********************* {} *********************'.format('States'))

        for i in range(len(self.game_states)):
            print('State {}: {}'.format(i, self.game_states[i]))

        print('**************************************************')

    def play_turn(self, board):

        old_board = list(board)

        if len(self.game_states) == 0 or len(self.get_next_states(get_n_of_tokens_on_board(board), board)) == 0:

            next_state = get_next_random_state(old_board, 1)
            self.add_game_state(next_state)
            next_place = get_place_of_token_to_get_to_next_state(board, next_state[0], 1)

            board[next_place] = 1

            self.display_game_states()

            return board

        else:

            next_state = self.get_next_greedy_state(get_n_of_tokens_on_board(board), board)
            self.add_game_state(next_state)
            next_place = get_place_of_token_to_get_to_next_state(board, next_state[0], 1)

            if next_place is not -1:
                board[next_place] = 1

            self.display_game_states()

            return board


def play():

    board = create_empty_board()

    agent = Agent()

    agent.play_turn(board)

    print(display_board(board))


if __name__ == '__main__':
    play()
