# This is contains duplicate + sliding window
# Not sure how to run it efficiently tho, this is my solution from neetcode's video

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(len(charSet), res)
        
        return res

