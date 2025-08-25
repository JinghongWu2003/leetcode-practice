class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j=0
        for i in range(len(nums)):
            if nums[j]!=val:
                # nums[j] = nums[i]
                j+=1
            elif nums[i]!=val:
                nums[j] = nums[i]
                nums[i] = val
                j+=1
        return j


if __name__ == "__main__":
    # ===== 测试用例 =====
    nums = [3, 2, 2, 3]
    val = 3
    sol = Solution()
    k = sol.removeElement(nums, val)
    print("Result length:", k)        # 期望输出: 2
    print("Modified nums:", nums[:k]) # 期望输出: [2, 2]

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    k = sol.removeElement(nums, val)
    print("Result length:", k)        # 期望输出: 5
    print("Modified nums:", nums[:k]) # 期望输出: [0,1,3,0,4]
