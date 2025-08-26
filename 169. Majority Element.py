class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand=None
        cnt=0
        for x in nums:
            if cnt==0:
                cand=x
                cnt=1
            elif x==cand:
                cnt+=1
            else:
                cnt-=1
        return cand