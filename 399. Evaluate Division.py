class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1.0
            if x == y:
                return 1
            visited.add(x)
            for nei, val in graph[x]:
                if nei in visited:
                    continue
                res = dfs(nei, y, visited)
                if res != -1.0:
                    return val * res
            return -1.0

        ans = []
        for a, b in queries:
            ans.append(dfs(a, b, set()))
        return ans
