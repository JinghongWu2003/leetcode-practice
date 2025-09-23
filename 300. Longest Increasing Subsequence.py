from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*(n+1)
        best=1
        # dp[0]=0
        for i in range(1, n):
            for j in range(i):
                if nums[j]< nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
                    best=max(dp[i],best)
        return best

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))