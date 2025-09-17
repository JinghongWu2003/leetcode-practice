from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # 把编号 num 映射到棋盘坐标 (row, col)
        def num_to_pos(num: int):
            row = (num - 1) // n
            col = (num - 1) % n
            r = n - 1 - row
            # 蛇形：偶数行（从下数）是左到右，奇数行是右到左
            if row % 2 == 0:
                c = col
            else:
                c = n - 1 - col
            return r, c

        # BFS
        q = deque([(1, 0)])  # (编号, 步数)
        visited = set([1])

        while q:
            cur, step = q.popleft()
            if cur == n * n:
                return step
            for dice in range(1, 7):
                nxt = cur + dice
                if nxt > n * n:
                    continue
                r, c = num_to_pos(nxt)
                if board[r][c] != -1:  # 有蛇/梯子
                    nxt = board[r][c]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, step + 1))
        return -1
