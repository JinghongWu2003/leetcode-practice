class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=1
        isSecond=False
        n=len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1] and not isSecond:
                nums[j]=nums[i]
                j+=1
                isSecond = True
            elif nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1
                isSecond=False
        return j


