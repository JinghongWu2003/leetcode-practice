class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        nums3 = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i = i + 1
            else:
                nums3.append(nums2[j])
                j = j + 1
        nums3.extend(nums1[i:m])
        nums3.extend(nums2[j:n])
        nums1[:]= nums3

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    sol = Solution()
    sol.merge(nums1, m, nums2, n)

    # print("Result:", nums1)  # 期望输出: [1,2,2,3,5,6]
