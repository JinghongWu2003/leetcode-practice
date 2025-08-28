class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]

        R = nums[-1]
        for i in range(n - 2, -1, -1):
            ans[i] = ans[i] * R
            R *= nums[i]

        return ans
