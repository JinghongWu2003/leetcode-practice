class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha={}
        l=0
        ans=0
        for r, c in enumerate(s):
            if c in alpha:
                alpha[c]+=1
                while alpha[c]>1:
                    alpha[s[l]]-=1
                    l+=1
            else:
                alpha[c]=1

            ans = max(ans,r-l+1)

        return ans

print(Solution().lengthOfLongestSubstring("tmmzuxt"))