class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        res=[]
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i]>0:
                break
            l,r=i+1,n-1
            while l<r:
                if nums[l]+nums[r]+nums[i]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    r -= 1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[r]+nums[i]>0:
                    r-=1
                else:
                    l+=1
        return res