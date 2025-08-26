class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        showup = {}
        for i in range(n):
            if nums[i] in showup:          # 修正 showpup -> showup
                showup[nums[i]] += 1
            else:
                showup[nums[i]] = 1        # 修正语法：冒号 -> =，并且初始化为 1

        max_count = -1                     # 避免覆盖 Python 内置函数 max
        max_key = None
        for key in showup:
            if showup[key] > max_count:    # 修正访问方式
                max_count = showup[key]
                max_key = key
        return max_key
