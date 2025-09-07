class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l=0
        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0
        ans=1
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                l+=1
            elif nums[i]-nums[i-1]==1:
                ans=max(ans,i-l+1)
            else:
                l=i
        return ans

