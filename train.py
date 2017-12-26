from agent import Agent, TrainedAgent
from board_drawer import display_board
from stopwatch import Stopwatch
from ttt_agent import create_empty_board, place_token_on_board, is_game_won, is_game_drawn

# 40000 --> 26min
# 20000 --> 10min
TRAINING_TURNS = 40000


def train():
    stopwatch = Stopwatch()
    stopwatch.start()

    board = create_empty_board()
    agent_plus = Agent(1, 0.2)
    agent_minus = Agent(-1, 0.2, 15)
    for i in range(TRAINING_TURNS):
        agent_plus.turn(board)

        if is_game_won(board, 1) or is_game_won(board, -1) or not is_game_drawn(board):
            # print(display_board(board))
            board = create_empty_board()
            agent_plus.turn(board)
        # print(agent_plus.states.txt)
        # print(display_board(board))
        agent_minus.turn(board)
        # place_token_on_board(board, int(input()), -1)
        # print(display_board(board))

        if is_game_won(board, 1) or is_game_won(board, -1) or not is_game_drawn(board):
            board = create_empty_board()
        if (i % 100) == 0:
            print('Iteration= {} of {}.'.format(i, TRAINING_TURNS))
            print('Training time= {}'.format(stopwatch.elapsed()))

    print('Training time= {}'.format(stopwatch.stop()))

    save_states_to_txt('states.txt', agent_plus.states)

    return agent_plus.states


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

        if is_game_won(board, 1) or is_game_won(board, -1) or not is_game_drawn(board):
            print(display_board(board))
            board = create_empty_board()
            agent.turn(board)
        # print(agent_plus.states.txt)
        print(display_board(board))
        place_token_on_board(board, int(input()), -1)
        print(display_board(board))

        if is_game_won(board, 1) or is_game_won(board, -1) or not is_game_drawn(board):
            board = create_empty_board()


if __name__ == '__main__':
    agent_states = train()
    trained_agent = TrainedAgent(agent_states, 1)
    #play_human(trained_agent)
