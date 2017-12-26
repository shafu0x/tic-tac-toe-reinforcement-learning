import unittest

from game.agent_helper import create_empty_board, n_tokens_on_board,place_token_on_board, state_value, Agent, place_to_get_to_state, \
    sub_board_from_board, empty_places_on_board, is_game_won, contains_one, state_all_null_except_one


class TestTicTacToeAgentMethods(unittest.TestCase):

    def test_create_empty_board(self):
        self.assertEqual(create_empty_board(), [0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_get_n_of_tokens_on_board(self):
        self.assertEqual(n_tokens_on_board([0, 0, 1, 0, -1, 0, 0, 0, 0]), 2)
        self.assertEqual(n_tokens_on_board([-1, 0, 1, 0, -1, 0, -1, 0, -1]), 5)
        self.assertEqual(n_tokens_on_board([0, 0, 0, 0, 0, 0, 0, 0, 0]), 0)
        self.assertEqual(n_tokens_on_board([1, -1, 1, 1, -1, -1, -1, -1, 1]), 9)

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

        agent.game_states = games_states

        self.assertEqual(agent.greedy(), [[0, 0, 0, 0, 0, 1, 0, 0, 0], [0.1]])

        agent = Agent()

        games_states = [[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]],
                        [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]],
                        [[0, 0, 0, 0, 0, 1, 0, 0, 0], [0.1]]]

        agent.game_states = games_states

        self.assertEqual(agent.greedy(), [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]])

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

    def test_calculate_new_game_state(self):

        agent = Agent()

        agent.previous_game_state = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]
        agent.current_game_state = [[0, 0, 0, 1, 0, -1, 0, 0, 0], [1]]

        self.assertEqual(agent.calculate_new_game_state_value(), [0.55])

    def test_contains_one(self):

        board1 = [1, 0, 0, 0, -1, 0, 0, 0, 1]

        self.assertEqual(contains_one(board1, -1), True)

        board2 = [1, 0, 0, 0, -1, 0, -1, 0, 1]

        self.assertEqual(contains_one(board2, -1), False)

        board3 = [1, 0, 0, 0, 1, 0, 0, 0, 1]

        self.assertEqual(contains_one(board3, -1), False)

        board4 = [-1, 0, -1, 0, -1, 0, 0, 0, 1]

        self.assertEqual(contains_one(board4, 1), True)

    def test_state_all_null_except_one(self):

        state1 = [1, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(state_all_null_except_one(state1), True)

        state2 = [1, 0, 0, 0, 0, -1, 0, 0, 0]

        self.assertEqual(state_all_null_except_one(state2), False)

        state3 = [0, 0, 0, 0, 0, 0, 1, 0, 0]

        self.assertEqual(state_all_null_except_one(state3), True)

if __name__ == '__main__':
    unittest.main()

