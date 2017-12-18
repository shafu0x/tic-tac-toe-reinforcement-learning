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


def tokens_on_board(board):

    counter = 0

    for token in board:
        if token == 1 or token == -1:
            counter += 1

    return counter


def place_token(board, place, token):
    board[place] = token


class Agent:

    def __init__(self):

        self.states = []

    def get_next_states(self, tokens_played):

        next_states = []

        for state in self.states:

            if tokens_on_board(state) == tokens_played + 1:
                next_states.append(state)

        return next_states

    @staticmethod
    def next_greedy_state(next_states):

        next_greedy_state = [[0], [0]]

        for state in next_states:
            if state[1] > next_greedy_state[1]:
                next_greedy_state = state

        return next_greedy_state

    @staticmethod
    def next_random_play(board):

        for i in range(8):
            if board[i] == 0:
                return i







