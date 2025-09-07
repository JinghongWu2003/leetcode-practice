class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        longest=0
        for x in s:
            if x-1 not in s:
                y=x
                length=1
                while y+1 in s:
                    length+=1
                    y+=1
                longest=max(longest, length)
        return longest