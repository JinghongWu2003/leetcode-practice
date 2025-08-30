class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1:
            return 1

        up = down = peak = 0
        ans = 1

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                down = 0
                ans += 1 + up
            elif ratings[i] == ratings[i - 1]:
                peak = up = down = 0
                ans += 1
            else:
                up = 0
                down += 1
                ans += down + 1 - (1 if down <= peak else 0)

        return ans

