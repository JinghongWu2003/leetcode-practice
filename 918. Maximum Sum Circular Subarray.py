class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0

        cur_max = 0
        cur_min = 0
        best = -math.inf
        worst = math.inf

        for x in nums:
            total += x
            cur_max = max(x, cur_max + x)
            best = max(best, cur_max)

            cur_min = min(x, cur_min + x)
            worst = min(cur_min, worst)

        if total == worst:
            return best
        else:
            return max(best, total - worst)