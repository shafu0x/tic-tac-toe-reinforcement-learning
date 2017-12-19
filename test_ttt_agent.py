import unittest
from tic_tac_toe_agent import create_empty_board, get_n_of_tokens_on_board, place_token_on_board, get_value_of_game_state, Agent


class TestTicTacToeAgentMethods(unittest.TestCase):

    def test_create_empty_board(self):
        self.assertEqual(create_empty_board(), [0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_get_n_of_tokens_on_board(self):
        self.assertEqual(get_n_of_tokens_on_board([0, 0, 1, 0, -1, 0, 0, 0, 0]), 2)
        self.assertEqual(get_n_of_tokens_on_board([-1, 0, 1, 0, -1, 0, -1, 0, -1]), 5)
        self.assertEqual(get_n_of_tokens_on_board([0, 0, 0, 0, 0, 0, 0, 0, 0]), 0)
        self.assertEqual(get_n_of_tokens_on_board([1, -1, 1, 1, -1, -1, -1, -1, 1]), 9)

    def test_place_token_on_board(self):
        self.assertEqual(place_token_on_board(create_empty_board(), 0, 1), [1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(place_token_on_board(create_empty_board(), 8, -1), [0, 0, 0, 0, 0, 0, 0, 0, -1])
        self.assertEqual(place_token_on_board(create_empty_board(), 2, 1), [0, 0, 1, 0, 0, 0, 0, 0, 0])
        self.assertEqual(place_token_on_board(create_empty_board(), 5, -1), [0, 0, 0, 0, 0, -1, 0, 0, 0])

        board = create_empty_board()
        board = place_token_on_board(board, 2, -1)
        board = place_token_on_board(board, 0, 1)
        board = place_token_on_board(board, 5, -1)
        board = place_token_on_board(board, 8, -1)

        self.assertEqual(board, [1, 0, -1, 0, 0, -1, 0, 0, -1])

        self.assertRaises(Exception, place_token_on_board, board, 2, -1)
        self.assertRaises(Exception, place_token_on_board, board, 0, 1)

    def test_get_value_of_game_state(self):

        self.assertEqual(get_value_of_game_state([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]), 0.5)
        self.assertEqual(get_value_of_game_state([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.85]]), 0.85)
        self.assertEqual(get_value_of_game_state([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1]]), 1)

    def test_get_next_states_for_agent(self):

        agent = Agent()

        games_states = [[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0]],
                        [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0]],
                        [[0, 0, 0, 0, 0, 1, 0, 0, 0], [0]],
                        [[1, 0, 0, 0, -1, 0, 0, 0, 0], [0]],
                        [[1, 0, 0, -1, 0, 0, 1, 0, 0], [0]],
                        [[1, 0, 0, -1, 0, 0, 1, 1, -1], [0]],
                        [[1, -1, 1, -1, 0, 0, 1, 1, -1], [0]]]

        agent.set_game_states(games_states)

        self.assertEqual(agent.get_next_states(0), [[[1, 0, 0, 0, 0, 0, 0, 0, 0], [0]],
                                                    [[0, 0, 0, 0, 0, 1, 0, 0, 0], [0]]])

        self.assertEqual(agent.get_next_states(1), [[[1, 0, 0, 0, -1, 0, 0, 0, 0], [0]]])


if __name__ == '__main__':
    unittest.main()
