class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        last_s, last_t = {}, {}
        if len(s) != len(pattern):
            return False

        return len(set(zip(s, pattern))) == len(set(s)) == len(set(pattern))
