class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 1:
            return strs[0]

        ans = strs[0]
        for i in range(1, n):
            if len(strs[i]) < len(ans):
                ans = ans[:len(strs[i])]
            for j in range(len(strs[i])):
                if j < len(ans):
                    if ans[j] != strs[i][j]:
                        ans = ans[:j]

        return ans


