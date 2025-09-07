class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sort_nums = sorted(nums)

        i, j = 0, len(nums)-1

        a,b=0,0

        while i < j:
            if sort_nums[i]+sort_nums[j]==target:
                a=sort_nums[i]
                b=sort_nums[j]
                break
            elif sort_nums[i]+sort_nums[j] < target:
                i+=1
            else:
                j-=1

        ans=[]
        for i in range(len(nums)):
            if nums[i]==a:
                ans.append(i)
            elif nums[i]==b:
                ans.append(i)
        return ans

print(Solution().twoSum([-3,4,3,90],0))
