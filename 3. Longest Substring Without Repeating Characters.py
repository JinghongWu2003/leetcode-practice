class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        l=0
        ans=0
        for r, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[l])
                l+=1
            seen.add(ch)
            ans=max(ans,r-l+1)
        return ans