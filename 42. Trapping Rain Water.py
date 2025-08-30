class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        m = max(height)

        mesh = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(height[i]):
                mesh[j][i] = 1

        ans = 0
        for i in range(m):
            cur = 0
            start = False
            for j in range(n - 1):
                if mesh[i][j] == 1 and mesh[i][j + 1] != 1 and not start:
                    start = True
                elif mesh[i][j] == 1 and start:
                    start = False
                    ans += cur
                    cur = 0
                    if mesh[i][j + 1] != 1:
                        start = True
                elif mesh[i][j] == 0 and start:
                    cur += 1
            if mesh[i][-1]==1 and start:
                ans += cur

        return ans

if __name__ == "__main__":
    # ===== 测试用例 =====
    nums = [4,2,0,3,2,5]
    sol = Solution()
    k = sol.trap(nums)
    print("Result length:", k)        # 期望输出: 2


