class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n <= 1:
            return 0

        step = 0
        cur_right = 0
        furthest = 0

        for i in range(n - 1):
            furthest = max(furthest, nums[i] + i)
            if cur_right == i:
                step += 1
                cur_right = furthest

        return step
