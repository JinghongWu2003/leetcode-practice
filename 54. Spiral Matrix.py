class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        count = 0
        dr = True
        n, m = len(matrix), len(matrix[0])

        def append(matrix, dr):
            n, m = len(matrix), len(matrix[0])
            if dr:
                for i in range(m):
                    ans.append(matrix[0][i])
                for i in range(1, n):
                    ans.append(matrix[i][-1])
            else:
                for i in range(m - 1, -1, -1):
                    ans.append(matrix[-1][i])
                for i in range(n - 2, -1, -1):
                    ans.append(matrix[i][0])

        while matrix and len(ans) < n * m:
            append(matrix, dr)
            if dr == True:
                dr = False
                matrix = [row[:-1] for row in matrix[1:]]
            else:
                dr = True
                matrix = [row[1:] for row in matrix[:-1]]

        return ans


matrix = [[7],[9],[6]]
print(Solution().spiralOrder(matrix))
