class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()
        start, end = intervals[0][0], intervals[0][1]
        ans = [[start, end]]
        j = 0
        for i in range(1, len(intervals)):
            # if intervals[i][0] <= end and intervals[i][1] >= start:
            if (intervals[i][0] > end or intervals[i][1] < start):
                start = intervals[i][0]
                end = intervals[i][1]
                ans.append([start, end])
                j += 1
            else:
                ans[j] = [min(start, intervals[i][0]), max(end, intervals[i][1])]
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])

        # start, end = ans[-1][0], ans[-1][1]
        # i=len(ans)-2
        # while i>=0:
        #     if (ans[i][0] > end or ans[i][1] < start):
        #         i-=1
        #     else:
        #         ans[i] = [min(start, ans[i][0]), max(end, ans[i][1])]
        #         start = min(start, ans[i][0])
        #         end = max(end, ans[i][1])
        #         del ans[i]
        #         i-=1
        return ans

print(Solution().merge([[2,3],[5,5],[2,2],[3,4],[3,4]]))