class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        cur = 0
        dir = -1  # 遇到两端翻转方向
        for ch in s:
            rows[cur] += ch
            if cur == 0 or cur == numRows - 1:
                dir *= -1
            cur += dir
        return ''.join(rows)
