# state = [[board], [value]]
from ttt_agent import n_tokens_on_board, sub_board_from_board, contains_one, state_all_null_except_one


class Agent:

    def __init__(self, token):
        self.pre_state = []
        self.current_state = []
        self.states = []
        self.token = token

    # if first state is added pre state is []
    def add_state(self, state):

        if state not in self.states:
            self.states.append(state)

            self.pre_state = self.current_state
            self.current_state = state

    # null --> []
    def next_states(self, board):
        next_states = []

        n_tokens_board = n_tokens_on_board(board)

        for state in self.states:
            sub_board = sub_board_from_board(state[0], board)
            n_tokens_state = n_tokens_on_board(state[0])

            if contains_one(sub_board, -self.token) \
                    and state_all_null_except_one(sub_board) \
                    and n_tokens_state > n_tokens_board:
                next_states.append(state)

        return next_states

    # null --> [[], [0]]
    def greedy(self, board):

        next_states = self.next_states(board)
        greedy = [[], [0]]
        for state in next_states:

            if state[1][0] > greedy[1][0]:
                greedy = state
        return greedy
