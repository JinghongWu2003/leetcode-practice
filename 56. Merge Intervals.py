class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])  # 只按左端点排
        merged = []
        for s, e in intervals:
            if not merged or s > merged[-1][1]:
                merged.append([s, e])
            else:
                merged[-1][1] = max(merged[-1][1], e)
        return merged

# 测试
print(Solution().merge([[2,3],[5,5],[2,2],[3,4],[3,4]]))  # -> [[2,4],[5,5]]
