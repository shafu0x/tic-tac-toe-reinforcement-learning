# state = [[board], [value]]
# TODO: use numpy array

from training.agent_helper import n_tokens_on_board, sub_board_from_board, contains_one, state_all_null_except_one, \
    get_next_random_state, place_to_get_to_state, is_game_won
from random import randint


class Agent:

    # random_turn 10 --> 10%
    def __init__(self, token, learning_rate=0.001, random_turns=10):
        self.pre_state = []
        self.current_state = []
        self.states = []
        self.token = token
        self.learning_rate = learning_rate
        self.random_turns = random_turns

    def add_state(self, new_state):
        self.states.append(new_state)

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

    def backprop_state_value(self):

        if not self.pre_state:
            return self.current_state
        else:
            state_value = self.pre_state[1][0] + (self.learning_rate * (self.current_state[1][0] - self.pre_state[1][0]))
            self.pre_state[1] = [state_value]
            return self.pre_state[1]

    def update_state(self, new_state):
        for state in self.states:
            if state[0] == new_state[0]:
                state[1] = new_state[1]

    def is_state_in_states(self, state):
        board_of_state = state[0]
        for state in self.states:
            if state[0] == board_of_state:
                return True
        return False

    def turn(self, board):
        prob_greedy = randint(0, 100)
        old_board = list(board)
        # new state
        if len(self.states) == 0 or prob_greedy < self.random_turns:
            next_state = get_next_random_state(board, self.token)
            self.add_state(next_state)
        else:
            next_state = self.greedy(board)

        if next_state == [[], [0]]:
            next_state = get_next_random_state(board, self.token)
            self.add_state(next_state)

        self.update_pre_and_current_state(next_state)
        p_t_n_s = place_to_get_to_state(old_board, next_state, self.token)
        board[p_t_n_s] = self.token

        if self.is_state_winning_state():
            self.current_state[1] = [1]
            self.update_state(self.current_state)

        if self.is_state_lost_state():
            self.current_state[1] = [0]
            self.update_state(self.current_state)
        return board

    def update_pre_and_current_state(self, next_state):
        if not self.pre_state:
            self.current_state = next_state
            self.pre_state = self.current_state
        else:
            self.pre_state = self.current_state
            self.current_state = next_state
        self.backprop_state_value()

    def is_state_winning_state(self):
        return is_game_won(self.current_state[0], self.token)

    def is_state_lost_state(self):
        return is_game_won(self.current_state[0], -self.token)

    def reset_both_states(self):
        self.pre_state = []
        self.current_state = []


class TrainedAgent:

    def __init__(self, states, token):
        self.states = states
        self.token = token

    def turn(self, board):
        old_board = list(board)
        next_state = self.greedy(board)
        p_t_n_s = place_to_get_to_state(old_board, next_state, self.token)
        board[p_t_n_s] = self.token

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

    def greedy(self, board):
        next_states = self.next_states(board)
        greedy = [[], [0]]
        for state in next_states:
            if state[1][0] > greedy[1][0]:
                greedy = state
        return greedy
