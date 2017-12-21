# _____________
# | 0 | 1 | 2 |
# _____________
# | 3 | 4 | 5 |
# _____________
# | 6 | 7 | 8 |
# _____________
#
from random import randint
from board_drawer import display_board


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
    if get_n_of_tokens_on_board(board) == 9 \
            and not is_game_won(board, 1)\
            and not is_game_won(board, -1):
        return False

    return True


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


def get_n_of_tokens_on_board(board):

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
    next_random_place = get_next_random_place(board)
    board[next_random_place] = token

    return create_state_from_board(board, [0.5])


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
        else:
            return 'place to get to next state was not found. board={}, next_game_state={}, token={}'.format(board, next_game_state, token)



class Agent:

    def __init__(self):

        self.game_states = []
        self.previous_game_state = []
        self.current_game_state = []
        self.learning_rate = 0.1
        self.game_state_index = 0

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

        return next_greedy_game_state

    def update_game_state_in_list(self, updated_game_state):
        for game_state in self.game_states:
            if game_state[0] == updated_game_state[0]:
                game_state[1] = updated_game_state[1]

    def calculate_new_game_state_value(self):
        new_game_state = self.previous_game_state[1][0] + (self.learning_rate * (self.current_game_state[1][0] - self.previous_game_state[1][0]))
        return [new_game_state]

    def update_game_state_value(self, game_state, game_state_value):
        game_state[0][1] = game_state_value
        return game_state

    def update_game_state_value_of_game_state_in_list(self):
        new_game_state_value = self.calculate_new_game_state_value()
        updated_game_state = self.update_game_state_value(self.previous_game_state, new_game_state_value)
        self.update_game_state_in_list(updated_game_state)

    def display_game_states(self):

        print('********************* {} *********************'.format('States'))

        for i in range(len(self.game_states)):
            print('State {}: {}'.format(i, self.game_states[i]))

        print('**************************************************')

    def play_turn(self, board):

        old_board = list(board)

        if self.no_next_state(board):

            next_state = get_next_random_state(old_board, 1)
            self.add_game_state(next_state)
            next_place = place_to_get_to_state(board, next_state, 1)

            board[next_place] = 1

            self.display_game_states()

            return board, next_state

        else:

            next_state = self.get_next_greedy_state(get_n_of_tokens_on_board(board), board)
            self.add_game_state(next_state)
            next_place = place_to_get_to_state(board, next_state, 1)

            if next_place is not -1:
                board[next_place] = 1

            self.display_game_states()

            return board, next_state

    def no_next_state(self, board):

        return len(self.game_states) == 0 or len(self.get_next_states(get_n_of_tokens_on_board(board), board)) == 0

    def get_value_of_board_state(self, board):

        for s in self.game_states:
            if s[0] == board:
                return s[1]


def play():

    board = create_empty_board()

    agent = Agent()

    for i in range(200):

        if len(agent.game_states) is not 0:
            agent.previous_game_state = agent.current_game_state

        _, next_state = agent.play_turn(board)
        agent.current_game_state = next_state

        if len(agent.game_states) is not 1:
            agent.update_game_state_value_of_game_state_in_list()

        print(display_board(board))

        if is_game_won(board, 1):
            agent.add_game_state(create_state_from_board(board, [1]))
            print(display_board(board))
            print('-------- X wins --------')
            board = create_empty_board()
            agent.play_turn(board)
            print(display_board(board))

        if is_game_drawn(board):
            print(display_board(board))
            print('-------- DRAW --------')
            board = create_empty_board()
            agent.play_turn(board)
            print(display_board(board))

        place_token_on_board(board, int(input()), -1)

        if is_game_won(board, -1):
            print(display_board(board))
            print('-------- O wins --------')
            board = create_empty_board()
            print(display_board(board))


if __name__ == '__main__':
   play()

