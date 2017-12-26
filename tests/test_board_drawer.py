import unittest

from game.board_drawer import display_board


class TestTTTBoardDrawer(unittest.TestCase):

    def test_display_board(self):

        board = [1, 0, 0, -1, -1, 1, 0, 0, -1]

        print(display_board(board))

        board = [0, 0, 1, -1, -1, 0, 0, 0, -1]

        print(display_board(board))
