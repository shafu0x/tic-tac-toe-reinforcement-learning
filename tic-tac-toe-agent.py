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


def number_of_tokens_on_board(board):

    counter = 0

    for token in board:
        if token == 1 or token == -1:
            counter += 1

    return counter


def place_token(board, place, token):
    board[place] = token


def next_random_play(board):

    for i in range(8):
        if board[i] == 0:
            board[i] = 1

    return board


def get_value_of_game_state(state):
    return state[1]


class Agent:

    def __init__(self):

        self.game_states = []
        self.previous_game_state_value = 0

    def get_next_states(self, tokens_played):

        next_game_states = []

        for game_state in self.game_states:

            if number_of_tokens_on_board(game_state) == tokens_played + 1:
                next_game_states.append(game_state)

        return next_game_states

    @staticmethod
    def next_greedy_state(next_game_states):

        next_greedy_game_state = [[0], [0]]

        for game_state in next_game_states:
            if game_state[1] > next_greedy_game_state[1]:
                next_greedy_game_state = game_state

        return next_greedy_game_state

    def play(self, board):

        return 0








