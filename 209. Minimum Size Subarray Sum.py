class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        s=0
        l=0
        ans=float('inf')

        for i, x in enumerate(nums):
            s+=x
            while s>=target:
                ans=min(ans, i-l+1)
                s-=nums[l]
                l+=1
        return 0 if ans==float('inf') else ans 