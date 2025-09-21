class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(32):
            bit_sum=0
            for x in nums:
                bit_sum+=(x>>i)&1
            if bit_sum%3:
                res|=(1<<i)
        if res>=1 <<31:
            res-=1<<32
        return res