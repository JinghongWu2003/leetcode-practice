class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()

        overlap=[[points[0][0],points[0][1]]]

        for i in range(1, len(points)):
            if overlap[-1][1] >= points[i][0]:
                overlap[-1]=[points[i][0], min(overlap[-1][1], points[i][1])]
            else:
                overlap.append([points[i][0],points[i][1]])

        return len(overlap)

print(Solution().findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))