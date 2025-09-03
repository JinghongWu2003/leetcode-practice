class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            for j in range(first, last):
                offset = j - first
                matrix[first][j], matrix[j][last], matrix[last][last - offset], matrix[last - offset][first] = \
                    matrix[last - offset][first], matrix[first][j], matrix[j][last], matrix[last][last - offset]
