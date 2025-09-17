class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True