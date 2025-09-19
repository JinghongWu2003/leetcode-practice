class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start: int):
            # 如果已经选满 k 个，收集结果并返回
            if len(path) == k:
                res.append(path[:])
                return

            remain = k - len(path)
            # 剪枝：x 最多到 n - remain + 1
            for x in range(start, n - remain + 2):  # 注意 range 右开
                path.append(x)      # 做选择
                dfs(x + 1)          # 递归
                path.pop()          # 撤销选择

        dfs(1)
        return res
