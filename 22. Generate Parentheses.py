class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res,path=[],[]
        open_used=closed_used=0
        def dfs(open_used,closed_used):
            if open_used==closed_used==n:
                res.append("".join(path))
                return

            if open_used<n:
                path.append("(")
                dfs(open_used+1,closed_used)
                path.pop()
            if closed_used<open_used:
                path.append(")")
                dfs(open_used,closed_used+1)
                path.pop()

        dfs(0,0)
        return res

