class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        # 直接和反转后的字符串比较
        return s == s[::-1]
