class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen and i- seen[nums[i]]<=k:
                return True
            elif nums[i] in seen and i- seen[nums[i]]>k:
                seen[nums[i]]=i
            else:
                seen[nums[i]]=i
        return False