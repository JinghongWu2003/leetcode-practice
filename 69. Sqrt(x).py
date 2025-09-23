class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l,r=0,x//2+1
        ans=1
        while l<=r:
            mid=(l+r)//2
            sq=mid*mid
            if sq==x:
                return mid
            if sq<x:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans