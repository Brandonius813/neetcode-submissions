# Wrong for loop syntax on line 8
# Tried to call range(len(int)) in lower forloop on strlen
# Tried to append onto a string in bottom res for loop.  Not how it works.
# Tried to INITIALIZE res with a blank string.  This led to output having an extra blank string at the end.  Fixed by moving to start of loop.

# My method breaks for strings with len over 9.  Single digit ints only... OOF.  Need to add another delimiter after the num to know how long?  Or I start with len, then add a hash?  And record length until I hit the hash.

# Even with my redesigned solution, I don't correctly add base-10 numbers.  If I had 11 as the length, I was adding 1+1.

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in range(len(strs)):
            encoded += str(len(strs[s]))
            encoded += "#"
            encoded += strs[s]
        
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        strLen = ""
        
        while i < len(s):
            strLen += s[i]
            i += 1

            if s[i] != "#":
                continue
            
            strLen = int(strLen)

            res.append("")
            i += 1
                        
            for c in range(strLen):
                res[-1] += s[i]
                i += 1
            
            strLen = ""
        
        return res
            

