class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        first_row = any(matrix[0][j] == 0 for j in range(n))
        first_col = any(matrix[j][0] == 0 for j in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0

        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        if first_col:
            for j in range(m):
                matrix[j][0] = 0
