from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for x in strs:
            cnt=[0]*26
            for s in x:
                cnt[ord(s) - ord('a')] += 1
            groups[tuple(cnt)].append(x)
        return list(groups.values())