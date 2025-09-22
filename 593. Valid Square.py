class Solution:

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        d = []
        d.append(dist(p1, p2))
        d.append(dist(p1, p3))
        d.append(dist(p1, p4))
        d.append(dist(p3, p2))
        d.append(dist(p4, p2))
        d.append(dist(p3, p4))
        d.sort()
        return d[0] > 0 and d[0] == d[1] == d[2] == d[3] and d[4] == d[5] and d[4] == 2 * d[0]





