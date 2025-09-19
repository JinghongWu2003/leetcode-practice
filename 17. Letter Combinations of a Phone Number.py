from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs","8": "tuv","9": "wxyz"
        }
        res = []
        path = []

        def dfs(idx: int):
            if idx == len(digits):
                res.append("".join(path))
                return
            for ch in phone[digits[idx]]:
                path.append(ch)          # 做选择
                dfs(idx + 1)             # 递归到下一位
                path.pop()               # 撤销选择（恢复现场）

        dfs(0)
        return res
