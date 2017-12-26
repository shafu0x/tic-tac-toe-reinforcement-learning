# Tic Tac Toe Reinforcement Learning

An agent who learns the game of tic tac toe using reinforcement learning

## How it works

An agent is trained by playing against an slightly different agent. The agent collects all states and finds. A state
contains a board and a state value.

```
[[[1, 0, 0, -1, 0, -1, 0, 1, 0]], [0.62]]
```

A new discovered state is given a state value of 0.5
A loosing state is given a state value of 0
A winning state is given a state value of 1

If the agent finds states that could be played it chooses the state with the highest state value. This is also called a
**greedy** turn. Every once in a while the agent chooses a **random** turn. This is determined by the random factor of
the agent

## How to train

In the train file following code can be run.
All parameters can be altered at the top of the file

'''
save_states = train()
trained_agent = TrainedAgent(save_states, 1)

#To play against the agent
play_human(trained_agent)
'''

## Authors

* **Sharif Elfouly** - [SharifElfouly](https://github.com/SharifElfouly)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Inspiration for this code came from Chapter 1 of the book Reinforcement Learning- An Introduction (Adaptive Computation and Machine Learning) by Sutton and Barto

