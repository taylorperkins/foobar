import unittest

from utils import print_time

from logic.doomsday_fuel import answer


class TestDoomsdayFuel(unittest.TestCase):
    """Challenge 3
    Doomsday Fuel
    =============

    Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved.
    It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable
    form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.

    Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end
    state of a given ore sample. You have carefully studied the different structures that the ore can take and which
    transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed.
    That is, each time the ore is in 1 state, it has the same probabilities of entering the next state
    (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have
    hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

    Write a function answer(m) that takes an array of array of nonnegative ints representing how many times
    that state has gone to the next state and return an array of ints for each terminal state giving the exact
    probabilities of each terminal state, represented as the numerator for each state, then the denominator for all
    of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which
    state the ore is in, there is a path from that state to a terminal state. That is, the processing will always
    eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer
    during the calculation, as long as the fraction is simplified regularly.

    For example, consider the matrix m:
    [
      [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
      [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
      [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
      [0,0,0,0,0,0],  # s3 is terminal
      [0,0,0,0,0,0],  # s4 is terminal
      [0,0,0,0,0,0],  # s5 is terminal
    ]

    So, we can consider different paths to terminal states, such as:
    s0 -> s1 -> s3
    s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
    s0 -> s1 -> s0 -> s5

    Tracing the probabilities of each, we find that
    s2 has probability 0
    s3 has probability 3/14
    s4 has probability 1/7
    s5 has probability 9/14

    So, putting that together, and making a common denominator, gives an answer in the form of
    [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
    [0, 3, 2, 9, 14].


    Test cases
    ==========

    Inputs:
        (int) m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    Output:
        (int list) [7, 6, 8, 21]

    Inputs:
        (int) m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    Output:
        (int list) [0, 3, 2, 9, 14]
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @print_time
    def test_example_1(self):
        response = answer([
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ])

        self.assertEqual(response, [0, 3, 2, 9, 14])

    @print_time
    def test_example_2(self):
        response = answer([
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])

        self.assertEqual(response, [7, 6, 8, 21])

    @print_time
    def test_example_3(self):
        response = answer([
            [1, 2, 3, 0, 0, 0],
            [4, 5, 6, 0, 0, 0],
            [7, 8, 9, 1, 0, 0],
            [0, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ])

        self.assertEqual(response, [1, 2, 3])

    @print_time
    def test_example_4(self):
        response = answer([
            [0]
        ])

        self.assertEqual(response, [1, 1])

    @print_time
    def test_example_5(self):
        response = answer([
            [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
            [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
            [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
            [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        self.assertEqual(response, [1, 2, 3, 4, 5, 15])

    @print_time
    def test_example_6(self):
        response = answer([
            [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
            [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
            [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
            [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
            [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        self.assertEqual(response, [4, 5, 5, 4, 2, 20])

    @print_time
    def test_example_7(self):
        response = answer([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        self.assertEqual(response, [1, 1, 1, 1, 1, 5])

    @print_time
    def test_example_8(self):
        response = answer([
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        self.assertEqual(response, [2, 1, 1, 1, 1, 6])

    @print_time
    def test_example_9(self):
        response = answer([
            [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
            [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
            [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        self.assertEqual(response, [6, 44, 4, 11, 22, 13, 100])

    @print_time
    def test_example_10(self):
        response = answer([
            [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
            [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
            [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
            [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
            [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        self.assertEqual(response, [1, 1, 1, 2, 5])
