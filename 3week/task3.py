"""
leetcode.com/problem-list/array/
https://leetcode.com/problems/rotate-image/submissions/1412730823/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()
