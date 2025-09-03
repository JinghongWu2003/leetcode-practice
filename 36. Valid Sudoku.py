class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]

        i = j = 0
        while i < 9:
            j=0
            while  j < 9:
                x, y = i, j
                block = {}
                while x < i + 3:
                    y=j
                    while y < j + 3:
                        if board[x][y] != '.':
                            if board[x][y] in row[x] or board[x][y] in block or board[x][y] in col[y]:
                                return False
                            else:
                                row[x][board[x][y]] = 1
                                col[y][board[x][y]] = 1
                                block[board[x][y]] = 1
                        y+=1
                    x+=1
                j += 3
            i += 3

        return True

