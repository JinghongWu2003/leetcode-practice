class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 2
        n = len(nums)

        if n <= 2:
            return n

        for i in range(2, n):
            if nums[i] != nums[j - 2]:
                if i != j:
                    nums[j] = nums[i]
                j += 1
        return j


