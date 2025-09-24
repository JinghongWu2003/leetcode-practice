class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        bestL, bestR = 0, 0
        for i in range(n):
            l1, r1 = expand(i, i)
            if r1 - l1 > bestR - bestL:
                bestR, bestL = r1, l1
            l2, r2 = expand(i, i + 1)
            if r2 - l2 > bestR - bestL:
                bestR, bestL = r2, l2
        return s[bestL:bestR + 1]
