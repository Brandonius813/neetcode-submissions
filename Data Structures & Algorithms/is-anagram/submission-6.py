class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = defaultdict(int)
        for c in s:
            sdict[c] += 1
        
        for c in t:
            sdict[c] -= 1
        
        if set(sdict.values()) == {0}:
            return True
        
        else:
            return False