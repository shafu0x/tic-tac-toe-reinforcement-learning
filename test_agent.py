import unittest
from agent import Agent


class TestAgent(unittest.TestCase):

    def test_add_state(self):

        state1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]
        state2 = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]]
        state3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]
        state4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.8]]
        state5 = [[0, 0, 0, 0, 0, -1, 0, 0, 0], [0.5]]

        agent = Agent()
        agent.add_state(state1)
        agent.add_state(state2)
        agent.add_state(state3)
        agent.add_state(state4)
        agent.add_state(state5)

        self.assertEqual(len(agent.states), 4)
        self.assertEqual(agent.current_state, state5)
        self.assertEqual(agent.pre_state, state4)

        state1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]
        state2 = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]]

        agent = Agent()
        agent.add_state(state1)
        agent.add_state(state2)
        self.assertEqual(agent.pre_state, state1)
        self.assertEqual(agent.current_state, state2)

    def test_next_state(self):

        board = [1, 0, 0, 0, 0, -1, 0, 0, 0]

        state1 = [[1, 0, 0, 1, 0, -1, 0, 0, 0], [0.5]]
        state2 = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]]
        state3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]
        state4 = [[1, 0, 0, 0, 0, -1, 0, 1, 0], [0.8]]

        agent = Agent()
        agent.add_state(state1)
        agent.add_state(state2)
        agent.add_state(state3)
        agent.add_state(state4)

        self.assertEqual(agent.next_states(board), [[[1, 0, 0, 1, 0, -1, 0, 0, 0], [0.5]],
                                                    [[1, 0, 0, 0, 0, -1, 0, 1, 0], [0.8]]])




