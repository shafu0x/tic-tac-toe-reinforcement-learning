import unittest
from ttt_agent import create_empty_board, get_n_of_tokens_on_board,place_token_on_board, state_value, Agent, place_to_get_to_state, \
    sub_board_from_board, empty_places_on_board, is_game_won


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

        self.assertEqual(state_value([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]), 0.5)
        self.assertEqual(state_value([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.85]]), 0.85)
        self.assertEqual(state_value([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1]]), 1)

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

        self.assertEqual(place_to_get_to_state(board, next_game_state, 1), 4)

        board = [1, 0, -1, 0, 0, 1, 0, 0, 0]

        next_game_state = [1, 0, -1, 0, 0, 1, 0, 1, 0]

        self.assertEqual(place_to_get_to_state(board, next_game_state, 1), 7)

    def test_subtract_list_from_list(self):

        list1 = [1, 0, 0]
        list2 = [0, 0, 1]

        self.assertEqual(sub_board_from_board(list1, list2), [-1, 0, 1])

        list1 = [1, 0, 0, 0]
        list2 = [0, 0, 1]

        self.assertRaises(Exception, sub_board_from_board, list1, list2)

        list1 = [1, 0, 0, 1, -1]
        list2 = [0, 0, 1, 0, -1]

        self.assertEqual(sub_board_from_board(list1, list2), [-1, 0, 1, -1, 0])

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

        self.assertEqual(empty_places_on_board(board), [0, 1, 2, 3, 6, 8])

        board = [1, -1, 1, 0, 1, -1, 1, 1, 0]

        self.assertEqual(empty_places_on_board(board), [3, 8])

    def test_is_game_won(self):

        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(is_game_won(board, 1), False)

        board = [1, 1, 1, 0, 0, 0, 0, 0, 0]

        self.assertEqual(is_game_won(board, 1), True)

        board = [1, 0, 0, 0, 1, 0, 0, 0, 1]

        self.assertEqual(is_game_won(board, 1), True)

        board = [1, 0, 0, 0, 1, 0, 0, 0, 1]

        self.assertEqual(is_game_won(board, -1), False)

    def test_update_game_state(self):

        agent = Agent()
        agent.add_game_state([[0, 0, 1], [0.5]])

        agent.update_game_state_in_list([[0, 0, 1], [1]])

        self.assertEqual(agent.game_states[0][1], [1])

        agent.add_game_state([[-1, 0, 1], [0.2]])

        agent.update_game_state_in_list([[-1, 0, 1], [0.75]])

        self.assertEqual(agent.game_states[1][1], [0.75])

    # TODO: REMOVE
    def test_update_previous_game_state_value(self):

        agent = Agent()

        p_game_state = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]

        c_game_state = [[0, 0, 0, 1, 0, -1, 0, 0, 0], [1]]

        self.assertEqual(agent.update_previous_game_state_value(p_game_state, c_game_state), [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.55]])

    def test_calculate_new_game_state(self):

        agent = Agent()

        agent.previous_game_state = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]
        agent.current_game_state = [[0, 0, 0, 1, 0, -1, 0, 0, 0], [1]]

        self.assertEqual(agent.calculate_new_game_state_value(), [0.55])

if __name__ == '__main__':
    unittest.main()

