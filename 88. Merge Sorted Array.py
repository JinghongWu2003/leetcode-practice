class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        last = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
                last -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
                last -= 1
        if i >= 0:
            nums1[:last+1] = nums1[:i+1]
        if j >= 0:
            nums1[:last+1] = nums2[:j+1]



if __name__ == "__main__":
    nums1 = [0]
    m = 0
    nums2 = [2]
    n = 1

    sol = Solution()
    sol.merge(nums1, m, nums2, n)

    print("Result:", nums1)  # 期望输出: [1,2,2,3,5,6]
