# test convert_FEN
import unittest
from utils.covert_FEN import convert_FEN


class TestConvertFEN(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            convert_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"),
            [
                "r",
                "n",
                "b",
                "q",
                "k",
                "b",
                "n",
                "r",
                "p",
                "p",
                "p",
                "p",
                "p",
                "p",
                "p",
                "p",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "P",
                "P",
                "P",
                "P",
                "P",
                "P",
                "P",
                "P",
                "R",
                "N",
                "B",
                "Q",
                "K",
                "B",
                "N",
                "R",
            ],
        )
