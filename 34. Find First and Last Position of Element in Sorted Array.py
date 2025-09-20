class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        left=l
        if left==len(nums) or nums[left]!=target:
            return [-1, -1]

        l, r = 0, len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]<=target:
                l=mid+1
            else:
                r=mid
        right = l-1
        return [left,right]