from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[[] for _ in range(len(triangle))]
        dp[0].append(triangle[0][0])

        n=len(triangle)
        for i in range(1,n):
            m=len(triangle[i])
            for j in range(m):
                if j>0 and j<m-1:
                    dp[i].append(min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j])
                if j==0:
                    dp[i].append(dp[i-1][0]+triangle[i][j])
                if j==m-1:
                    dp[i].append(dp[i-1][-1]+triangle[i][j])
        res=100001
        for x in dp[-1]:
            res=min(res,x)
        return res

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))