# Tic-Tac-Toe-Reinforcement-Learning
An agent who learns the game of tic tac toe using reinforcement learning

States are two dimensional arrays that contain a board and state value.
For example: [[1, 0, 0, -1, 0, -1, 0, 1, 0], [0.5]]

An agent keeps track of a current and previous state. After a turn the pre state value is updated with following equation:

# updated pre state value = pre state value + learning rate * (current state value - pre state value)
