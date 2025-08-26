class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        kk=k%n

        if kk==0:
            return nums

        nums1=[0]*n
        nums1[:kk]=nums[-kk:]
        nums1[kk:]=nums[:-kk]
        nums[:]=nums1[:]
