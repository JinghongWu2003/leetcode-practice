class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:  # ← 和前一个比
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:  # ← 和后一个比
                        r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return res
