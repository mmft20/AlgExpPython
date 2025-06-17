from AlgoExpertSolution.GreedyAlgorithms.MinimumWaitingTime import Program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        queries = [3, 2, 1, 2, 6]
        expected = 17
        actual = Program.minimumWaitingTime(queries)
        self.assertEqual(actual, expected)