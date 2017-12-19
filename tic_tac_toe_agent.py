from random import randint

winning_state = [[[1, 1, 1, 0, 0, 0, 0, 0, 0], [1]],
                 [[0, 0, 0, 1, 1, 1, 0, 0, 0], [1]],
                 [[0, 0, 0, 0, 0, 0, 1, 1, 1], [1]],
                 [[1, 0, 0, 0, 1, 0, 0, 0, 1], [1]],
                 [[0, 0, 1, 0, 1, 0, 0, 0, 1], [1]],
                 [[1, 0, 0, 1, 0, 0, 1, 0, 0], [1]],
                 [[0, 1, 0, 0, 1, 0, 0, 1, 0], [1]],
                 [[0, 0, 1, 0, 0, 1, 0, 0, 1], [1]]]


def create_empty_board():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0]


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

    def get_next_states(self, tokens_played):

        next_game_states = []

        for game_state in self.game_states:

            board = game_state[0]

            if get_n_of_tokens_on_board(board) == tokens_played + 1:
                next_game_states.append(game_state)

        return next_game_states

    def get_next_greedy_state(self, next_game_states):

        next_greedy_game_state = [[0], [0]]

        for game_state in next_game_states:
            if game_state[1] > next_greedy_game_state[1]:
                next_greedy_game_state = game_state

        return next_greedy_game_state[0]

    def display_game_states(self):

        print('********************* {} *********************'.format('States'))

        for i in range(len(self.game_states)):
            print('State {}: {}'.format(i, self.game_states[i]))

        print('**************************************************')


def subtract_list_from_list(list1, list2):

    if len(list1) is not len(list2):
        raise Exception

    new_list = []

    for i in range(len(list1)):
        new_element = list2[i] - list1[i]
        new_list.append(new_element)

    return new_list

a = Agent()

a.add_game_state([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]])
a.add_game_state([[0, 0, 0, 0, 0, 0, 1, 0, 0], [0.15]])
a.add_game_state([[0, 0, 0, -1, 0, 0, 0, 0, 0], [0.8]])

a.display_game_states()
