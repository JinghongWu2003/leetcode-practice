class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(K):
            if K<0: return 0
            ans=0
            l=odd=0

            for r, x in enumerate(nums):
                odd+=x&1
                while odd>K:
                    odd-=nums[l]&1
                    l+=1
                ans+=r-l+1
            return ans
        return at_most(k)-at_most(k-1)