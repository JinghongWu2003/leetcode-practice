class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        array = s.strip().split()
        l = 0
        r = len(array) - 1

        while l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

        return " ".join(array)
