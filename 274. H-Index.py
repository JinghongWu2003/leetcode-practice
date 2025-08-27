class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        bucket = [0] * (n + 1)

        for i in range(n):
            bucket[min(citations[i], n)] += 1

        s = 0

        for i in range(n, -1, -1):
            s += bucket[i]
            if s >= i:
                return i

        return 0