class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        furthest = 0
        cur_right = 0

        for i in range(len(nums)):
            if cur_right < i:
                step += 1
                cur_right = furthest
            furthest = max(furthest, nums[i] + i)

        return step