class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        n, m = len(t), len(s)
        if m == 0:
            return True
        i = j = 0
        while i < n:
            if t[i] == s[j]:
                j += 1
                if j == m:
                    return True
            i += 1
        return False
