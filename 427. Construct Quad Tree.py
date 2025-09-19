# Definition for a QuadTree node.
# class Node:
#     def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight

from typing import List

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        n = len(grid)

        def build(r0: int, c0: int, size: int) -> 'Node':
            # 1) 检查当前子区域是否全相等（全 0 或全 1）
            first = grid[r0][c0]
            uniform = True
            for i in range(r0, r0 + size):
                if not uniform:
                    break
                row = grid[i]
                for j in range(c0, c0 + size):
                    if row[j] != first:
                        uniform = False
                        break

            # 2) 如果统一，返回叶子节点
            if uniform:
                return Node(bool(first), True, None, None, None, None)

            # 3) 否则继续分成四块递归
            half = size // 2
            tl = build(r0,         c0,         half)
            tr = build(r0,         c0 + half,  half)
            bl = build(r0 + half,  c0,         half)
            br = build(r0 + half,  c0 + half,  half)

            # 非叶子节点的 val 任意（True/False 都行，评测不看）
            return Node(True, False, tl, tr, bl, br)

        return build(0, 0, n)
