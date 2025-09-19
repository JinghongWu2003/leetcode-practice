class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def dfs(left):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for x in left:
                path.append(x)
                dfs(left - {x})
                path.pop()

        dfs(set(nums))
        return res

