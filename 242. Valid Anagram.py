class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        base = ord('a')
        for i in range(len(s)):
            cnt[ord(s[i]) - base] += 1
            cnt[ord(t[i]) - base] -= 1
        return all(c == 0 for c in cnt)

