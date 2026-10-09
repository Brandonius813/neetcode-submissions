class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] += 1
        
        for i in range(len(t)):
            countT[t[i]] += 1
        
        if countS == countT:
            return True
        
        else:
            return False
