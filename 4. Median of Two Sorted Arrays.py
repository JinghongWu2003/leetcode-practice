from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKth(a: List[int], b: List[int], k: int) -> int:
            # 保证 a 更短，简化边界
            if len(a) > len(b):
                return getKth(b, a, k)
            if not a:                 # a 为空
                return b[k-1]
            if k == 1:                # 要找最小的那个
                return min(a[0], b[0])

            i = min(len(a), k // 2)
            j = k - i
            if a[i-1] <= b[j-1]:
                # 丢掉 a 的前 i 个
                return getKth(a[i:], b, k - i)
            else:
                # 丢掉 b 的前 j 个
                return getKth(a, b[j:], k - j)

        m, n = len(nums1), len(nums2)
        tot = m + n
        if tot % 2 == 1:
            return float(getKth(nums1, nums2, tot // 2 + 1))
        else:
            left = getKth(nums1, nums2, tot // 2)
            right = getKth(nums1, nums2, tot // 2 + 1)
            return (left + right) / 2.0
