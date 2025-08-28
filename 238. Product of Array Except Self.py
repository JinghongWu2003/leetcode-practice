class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left, right = [1] * n, [1] * n

        ans = [0] * n

        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]

        ans[0] = right[0]
        ans[-1] = left[n - 1]

        for i in range(1, n - 1):
            ans[i] = left[i] * right[i]

        return ans


