class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        freq = [0]*26
        for ch in magazine:
            freq[ord(ch)-97] += 1
        for ch in ransomNote:
            k = ord(ch)-97
            freq[k] -= 1
            if freq[k] < 0:
                return False
        return True
