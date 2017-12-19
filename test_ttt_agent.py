import unittest
from tic_tac_toe_agent import create_empty_board, get_n_of_tokens_on_board,place_token_on_board, get_value_of_game_state, Agent, get_place_of_token_to_get_to_next_state, \
    subtract_list_from_list, get_empty_places_on_board


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

    def test_get_next_greedy_state(self):

        agent = Agent()

        games_states = [[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]],
                        [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]],
                        [[0, 0, 0, 0, 0, 1, 0, 0, 0], [0.1]],
                        [[1, 0, 0, 0, -1, 0, 0, 0, 0], [0]],
                        [[1, 0, 0, -1, 0, 0, 1, 0, 0], [0.8]],
                        [[1, 0, 0, -1, 0, 0, 1, 1, -1], [0.98]],
                        [[1, -1, 1, -1, 0, 0, 1, 1, -1], [0.001]]]

        self.assertEqual(agent.get_next_greedy_state(games_states), [1, 0, 0, -1, 0, 0, 1, 1, -1])

        games_states = [[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]],
                        [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]],
                        [[0, 0, 0, 0, 0, 1, 0, 0, 0], [0.1]]]

        self.assertEqual(agent.get_next_greedy_state(games_states), [1, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_get_place_of_token_to_get_to_next_state(self):

        board = [0, 0, 0, 0, 0, 1, 0, 0, 0]

        next_game_state = [0, -1, 0, 0, 1, 1, 0, 0, 0]

        self.assertEqual(get_place_of_token_to_get_to_next_state(board, next_game_state, 1), 4)

        board = [1, 0, -1, 0, 0, 1, 0, 0, 0]

        next_game_state = [1, 0, -1, 0, 0, 1, 0, 1, 0]

        self.assertEqual(get_place_of_token_to_get_to_next_state(board, next_game_state, 1), 7)

    def test_subtract_list_from_list(self):

        list1 = [1, 0, 0]
        list2 = [0, 0, 1]

        self.assertEqual(subtract_list_from_list(list1, list2), [-1, 0, 1])

        list1 = [1, 0, 0, 0]
        list2 = [0, 0, 1]

        self.assertRaises(Exception, subtract_list_from_list, list1, list2)

        list1 = [1, 0, 0, 1, -1]
        list2 = [0, 0, 1, 0, -1]

        self.assertEqual(subtract_list_from_list(list1, list2), [-1, 0, 1, -1, 0])

    def test_add_game_state(self):

        agent = Agent()

        game_state = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]

        agent.add_game_state(game_state)

        self.assertEqual(agent.game_states, [[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]])

        agent.add_game_state([[1, -1, 1, -1, 0, 0, 1, 1, -1], [0.001]])

        self.assertEqual(agent.game_states, [[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]],
                                             [[1, -1, 1, -1, 0, 0, 1, 1, -1], [0.001]]])

        agent.add_game_state(game_state)

        self.assertEqual(agent.game_states, [[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]],
                                             [[1, -1, 1, -1, 0, 0, 1, 1, -1], [0.001]]])

    def test_get_empty_places_on_board(self):

        board = [0, 0, 0, 0, 1, -1, 0, 1, 0]

        self.assertEqual(get_empty_places_on_board(board), [0, 1, 2, 3, 6, 8])

        board = [1, -1, 1, 0, 1, -1, 1, 1, 0]

        self.assertEqual(get_empty_places_on_board(board), [3, 8])

if __name__ == '__main__':
    unittest.main()
