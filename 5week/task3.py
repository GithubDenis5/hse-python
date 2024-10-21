class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def iNeedMoreZeroes(matrix: list[list[int]], pos: list[int]) -> None:
            # ----
            for i in range(m):
                matrix[pos[0]][i] = 0
            # |
            for i in range(n):
                matrix[i][pos[1]] = 0

        n = len(matrix)
        m = len(matrix[0])

        zeroPos = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeroPos.append([i, j])

        for pos in zeroPos:
            iNeedMoreZeroes(matrix, pos)

        print(matrix)
