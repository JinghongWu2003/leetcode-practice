class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        j = 0
        dj = [nums[0]]

        for i in range(1, len(nums)):
            if i <= dj[j]:
                if nums[i] + i > dj[j]:
                    dj.append(nums[i] + i)
                    j += 1

        if dj[-1] >= len(nums) - 1:
            return True
        else:
            return False
