class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        l = 0
        ans = []
        if len(nums) <1:
            return ans

        def ops(l, r):
            if l == r:
                ans.append(str(nums[l]))
            else:
                ans.append(str(nums[l]) + "->" + str(nums[r]))

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                continue
            else:
                ops(l, i - 1)
                l = i
        ops(l, len(nums) - 1)
        return ans
print(Solution().summaryRanges([]))