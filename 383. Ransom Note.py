class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        i=j=0
        dict={}
        for i in range(len(magazine)):
            if magazine[i] in dict:
                dict[magazine[i]]+=1
            else:
                dict[magazine[i]]=1
        for i in range(len(ransomNote)):
            if ransomNote[i] in dict:
                dict[ransomNote[i]]-=1
                if dict[ransomNote[i]]<0:
                    return False
            else:
                return False
        return True
