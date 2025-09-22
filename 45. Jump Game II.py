class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        step = 0
        curEnd = 0
        curFurthest = 0

        for i in range(n - 1):
            curFurthest = max(curFurthest, i + nums[i])
            if curEnd == i:
                step += 1
                curEnd = curFurthest
                if curEnd >= n - 1:
                    break
        return step
