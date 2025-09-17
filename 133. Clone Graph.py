# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        old_to_new = {}

        def dfs(cur: 'Node') -> 'Node':
            # 若已克隆，直接返回克隆节点
            if cur in old_to_new:
                return old_to_new[cur]

            # 创建当前节点的克隆（先不处理邻居）
            copy = Node(cur.val)
            old_to_new[cur] = copy

            # 递归克隆邻居，并加到copy.neighbors
            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)

