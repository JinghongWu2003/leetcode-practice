class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        i, n = 0, len(intervals)
        s, e = newInterval

        # 1) 左侧：end < s
        while i < n and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1

        # 2) 重叠：intervals[i].start <= e
        while i < n and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1
        res.append([s, e])

        # 3) 右侧：剩余的都加进去
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

# 示例
print(Solution().insert([[1,5]], [0,0]))  # [[1,5],[6,8]]
