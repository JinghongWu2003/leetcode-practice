class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def up2low(char):
            if 'A' <= char <= 'Z':
                return chr(ord(char) - ord('A') + ord('a'))
            elif 'a' <= char <= 'z':
                return char
            else:
                return ''

        processed_s = ''

        for char in s:
            processed_s += up2low(char)

        l = len(processed_s) - 1
        r = 0
        while l > r:
            if processed_s[l] != processed_s[r]:
                return False
            l -= 1
            r += 1

        return True

print(Solution().isPalindrome("0P"))