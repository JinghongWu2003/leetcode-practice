class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)

        if n <= 1:
            return strs[0]

        ans = strs[0]

        for s in strs[1:]:
            j = 0
            while j < len(ans) and j < len(s) and ans[j] == s[j]:
                j += 1
            ans = ans[:j]
            if not ans:
                return ""

        return ans
