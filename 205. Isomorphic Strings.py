class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        last_s,last_t={},{}

        for i in range(len(s)):
            if last_s.get(s[i],-1)!=last_t.get(t[i],-1):
                return False
            last_s[s[i]]=last_t[t[i]]=i
        return True