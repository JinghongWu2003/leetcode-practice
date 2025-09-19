class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(l,h):
            if l>h:
                return l
            mid=(h+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return search(l,mid-1)
            elif nums[mid]<target:
                return search(mid+1,h)
        return search(0,len(nums)-1)

