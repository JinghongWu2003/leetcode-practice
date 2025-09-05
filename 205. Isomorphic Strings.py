class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        mapping = {}
        vers_mapping = {}
        for i in range(n):
            if t[i] in vers_mapping:
                if s[i] != vers_mapping[t[i]]:
                    return False
            if s[i] in mapping:
                if t[i] != mapping[s[i]]:
                    return False
            else:
                mapping[s[i]] = t[i]
                vers_mapping[t[i]] = s[i]
        return True

