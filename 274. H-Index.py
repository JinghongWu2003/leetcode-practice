class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()

        h = 0
        n = len(citations)
        for i in range(n):
            h = max(h, min(n - i, citations[i]))

        return h
