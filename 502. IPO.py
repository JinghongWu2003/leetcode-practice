class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects=sorted(zip(capital,profits))
        n=len(projects)
        i=0
        maxheap=[]

        for _ in range (k):
            while i<n and projects[i][0]<=w:
                _,p = projects[i]
                heapq.heappush(maxheap,-p)
                i+=1

            if not maxheap:
                break

            w+=-heapq.heappop(maxheap)

        return w