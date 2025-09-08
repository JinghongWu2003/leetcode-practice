class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in pairs.values():  # 左括号
                stack.append(ch)
            elif ch in pairs:  # 右括号
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                # 如果输入里可能有非括号字符
                return False

        return not stack
