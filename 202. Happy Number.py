class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def nxt(x):
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = nxt(n)
        return n == 1
