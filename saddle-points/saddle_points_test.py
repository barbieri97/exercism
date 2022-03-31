"""Tests for the saddle-points exercise

Implementation note:
The saddle_points function must validate the input matrix and raise a
ValueError with a meaningful error message if the matrix turns out to be
irregular.
"""
import unittest

from saddle_points import (
    saddle_points, create_colums,
    is_irregular, get_indexs_maxs_numbers
)

# Tests adapted from `problem-specifications//canonical-data.json`

# my personal tests

# class MyPernosalTests(unittest.TestCase):

#     def test_func_is_irregular(self):
#         matrixs = [[[1,2,3],[4,5,6],[1,2]], [[1,2,3],[4,5,6],[7,8,9]], [[1], [1], [1,2]]]
#         results = [False, True, False]
#         self.assertListEqual(results, [item for item in map(is_irregular, matrixs)])
    
#     def test_func_get_indexs_maxs_numbers(self):
#         rows = [
#             [1,4,7,7],
#             [1,2,3],
#             [5,2,1,1],
#             [5,5,5]
#         ]
#         results = [
#             [(2,7), (3,7)],
#             [(2,3)],
#             [(0,5)],
#             [(0,5), (1,5), (2,5)]
#         ]
#         self.assertListEqual(results, [item for item in map(get_indexs_maxs_numbers, rows)])
    
#     def test_func_create_colums(self):
#         matrixs = [
#             [[1,2,3],[4,5,6,],[7,8,9]],
#             [[1], [2], [3]],
#             [[1,2]]
#         ]
#         results = [
#             [[1,4,7], [2,5,8], [3,6,9]],
#             [[1,2,3]],
#             [[1], [2]]
#         ]
#         self.assertListEqual(results, [item for item in map(create_colums, matrixs)])

def sorted_points(point_list):
    return sorted(point_list, key=lambda p: (p["row"], p["column"]))


class SaddlePointsTest(unittest.TestCase):
    def test_can_identify_single_saddle_point(self):
        matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
        self.assertEqual(
            sorted_points(saddle_points(matrix)),
            sorted_points([{"row": 2, "column": 1}]),
        )

    def test_can_identify_that_empty_matrix_has_no_saddle_points(self):
        matrix = []
        self.assertEqual(sorted_points(saddle_points(matrix)), sorted_points([]))

    def test_can_identify_lack_of_saddle_points_when_there_are_none(self):
        matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
        self.assertEqual(sorted_points(saddle_points(matrix)), sorted_points([]))

    def test_can_identify_multiple_saddle_points_in_a_column(self):
        matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
        self.assertEqual(
            sorted_points(saddle_points(matrix)),
            sorted_points(
                [
                    {"row": 1, "column": 2},
                    {"row": 2, "column": 2},
                    {"row": 3, "column": 2},
                ]
            ),
        )

    def test_can_identify_multiple_saddle_points_in_a_row(self):
        matrix = [[6, 7, 8], [5, 5, 5], [7, 5, 6]]
        self.assertEqual(
            sorted_points(saddle_points(matrix)),
            sorted_points(
                [
                    {"row": 2, "column": 1},
                    {"row": 2, "column": 2},
                    {"row": 2, "column": 3},
                ]
            ),
        )

    def test_can_identify_saddle_point_in_bottom_right_corner(self):
        matrix = [[8, 7, 9], [6, 7, 6], [3, 2, 5]]
        self.assertEqual(
            sorted_points(saddle_points(matrix)),
            sorted_points([{"row": 3, "column": 3}]),
        )

    def test_can_identify_saddle_points_in_a_non_square_matrix(self):
        matrix = [[3, 1, 3], [3, 2, 4]]
        self.assertEqual(
            sorted_points(saddle_points(matrix)),
            sorted_points([{"row": 1, "column": 3}, {"row": 1, "column": 1}]),
        )

    def test_can_identify_that_saddle_points_in_a_single_column_matrix_are_those_with_the_minimum_value(
        self,
    ):
        matrix = [[2], [1], [4], [1]]
        self.assertEqual(
            sorted_points(saddle_points(matrix)),
            sorted_points([{"row": 2, "column": 1}, {"row": 4, "column": 1}]),
        )

    def test_can_identify_that_saddle_points_in_a_single_row_matrix_are_those_with_the_maximum_value(
        self,
    ):
        matrix = [[2, 5, 3, 5]]
        self.assertEqual(
            sorted_points(saddle_points(matrix)),
            sorted_points([{"row": 1, "column": 2}, {"row": 1, "column": 4}]),
        )

    # Additional tests for this track

    def test_irregular_matrix(self):
        matrix = [[3, 2, 1], [0, 1], [2, 1, 0]]
        with self.assertRaises(ValueError) as err:
            saddle_points(matrix)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "irregular matrix")

if __name__ == "__main__":
    unittest.main()
