class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(m):
            for j in range(n):
                cnt = 0
                for di, dj in dir:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and (board[x][y] & 1):
                        cnt += 1
                if (board[i][j] & 1) and 2 <= cnt <= 3:
                    board[i][j] |= 2
                if not (board[i][j] & 1) and cnt == 3:
                    board[i][j] |= 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
