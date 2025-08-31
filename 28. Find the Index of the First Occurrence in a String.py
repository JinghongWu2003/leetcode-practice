class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(needle)
        n = len(haystack)

        if m == 0:
            return 0
        elif n < m:
            return -1

        lsp = [0] * m
        i = 1
        perf = 0
        while i < m:
            if needle[i] == needle[perf]:
                perf += 1
                lsp[i] = perf
                i += 1
            elif perf > 0:
                perf = lsp[perf - 1]
            else:
                lsp[i] = 0
                i += 1

        i = 0
        perf = 0
        while i < n:
            if haystack[i] == needle[perf]:
                i += 1
                perf += 1
                if perf == m:
                    return i - m
            else:
                if perf > 0:
                    perf = lsp[perf - 1]
                else:
                    i += 1
        return -1

if __name__ == "__main__":
    k = Solution().strStr('aaa','aaa')
    print("Result length:", k)        # 期望输出: 2


