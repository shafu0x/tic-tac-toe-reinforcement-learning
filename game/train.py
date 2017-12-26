from game.agent import Agent, TrainedAgent
from game.agent_helper import create_empty_board, is_game_over, place_token_on_board
from game.board_drawer import display_board
from tools.stopwatch import Stopwatch

# 40000 --> 26min
# 20000 --> 10min
TRAINING_TURNS = 500
LEARNING_RATE = 0.2
AGENT_X_RANDOM_TURNS = 10
AGENT_O_RANDOM_TURNS = 25


def train():
    stopwatch = Stopwatch()
    stopwatch.start()

    board = create_empty_board()
    agent_x = Agent(1, LEARNING_RATE, AGENT_X_RANDOM_TURNS)
    agent_o = Agent(-1, LEARNING_RATE, AGENT_O_RANDOM_TURNS)
    for i in range(TRAINING_TURNS):
        agent_x.turn(board)
        if is_game_over(board):
            board = create_empty_board()
            agent_x.turn(board)
        agent_o.turn(board)
        if is_game_over(board):
            board = create_empty_board()
        if (i % 100) == 0:
            print('Iteration= {} of {}.'.format(i, TRAINING_TURNS))
            print('Training time= {}'.format(stopwatch.elapsed()))
    return agent_x.states


def save_states_to_txt(file, states):
    f = open(file, 'w')
    for state in states:
        f.write(str(state))
        f.write('\n')
    f.close()


def play_human(agent):
    board = create_empty_board()
    for i in range(1000):
        agent.turn(board)
        if is_game_over(board):
            print(display_board(board))
            board = create_empty_board()
            agent.turn(board)
        print(display_board(board))
        place_token_on_board(board, int(input()), -1)
        print(display_board(board))
        if is_game_over(board):
            board = create_empty_board()


if __name__ == '__main__':
    agent_states = train()
    save_states_to_txt('txt\states.txt', agent_states)
    trained_agent = TrainedAgent(agent_states, 1)
