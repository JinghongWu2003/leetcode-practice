class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict=[0]*26
        for x in s:
            index=ord(x)-ord('a')
            dict[index]+=1
        for x in t:
            index=ord(x)-ord('a')
            dict[index]-=1

        for x in dict:
            if x!=0:
                return False
        return True
print(Solution().isAnagram("cba", "cbd"))