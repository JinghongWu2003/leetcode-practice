class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
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

        th = num / 1000
        hun = num % 1000 / 100
        ten = num % 100 / 10
        sin = num % 10

        ans = []

        def judge(high, mid, low, num):
            if num == 9:
                ans.append(low + high)
            elif num < 9 and num > 4:
                ans.append(mid)
                for i in range(num - 5):
                    ans.append(low)
            elif num == 4:
                ans.append(low + mid)
            else:
                for i in range(num):
                    ans.append(low)

        for i in range(th):
            ans.append('M')

        judge('M', 'D', 'C', hun)
        judge('C', 'L', 'X', ten)
        judge('X', 'V', 'I', sin)

        roman_str = "".join(ans)

        return roman_str        