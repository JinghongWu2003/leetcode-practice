class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        def get_val(char):
            if char == 'I':
                return 1
            elif char == 'V':
                return 5
            elif char == 'X':
                return 10
            elif char == 'L':
                return 50
            elif char == 'C':
                return 100
            elif char == 'D':
                return 500
            else:
                return 1000

        n = len(s)

        ans = get_val(s[0])

        for i in range(1, n):
            if get_val(s[i]) > get_val(s[i - 1]):
                ans -= get_val(s[i - 1])
                ans += get_val(s[i]) - get_val(s[i - 1])
            else:
                ans += get_val(s[i])

        return ans

