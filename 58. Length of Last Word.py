class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = 0
        flag = True
        n = len(s)

        for i in range(n):
            if s[i] == ' ':
                flag = True
            elif flag and s[i] != ' ':
                cur = 1
                flag = False
            else:
                cur += 1

        return cur


# return len(s.strip().split()[-1])