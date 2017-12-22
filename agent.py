# state = [[board], [value]]
from ttt_agent import n_tokens_on_board


class Agent:

    def __init__(self):
        self.pre_state = []
        self.current_state = []
        self.states = []

    # if first state is added pre state is []
    def add_state(self, state):

        if state not in self.states:
            self.states.append(state)

            self.pre_state = self.current_state
            self.current_state = state

    def next_states(self, board):

        # TODO: substract board from each state and look for one -1

        pass

