# If I find an "open" parenthesees, I need to track it.
# If I find a "closed" parenthesees, I need to know that it's corresponding open is the most recent thing I saw.

# I think I'll make a stack of the inverse of what I see.  So if I see an open parens, hit up my hashmap, and add its VALUE to the stack.  Repeat until I find something that's not in the keys of my parens array.  If it's not there, then is it the most recent thing in my stack?  If yes, pop it off the stack, continue.  

# If I empty the stack and finish the input string, valid.

# I missed the edge case of only having closes.  Breaks my "stack -1" check.

class Solution:
    def isValid(self, s: str) -> bool:
        parens = {"(":")", "{":"}", "[":"]"}
        stack = []

        for c in range(len(s)):
            if s[c] in parens:
                stack.append(parens[s[c]])

            else:
                if stack and s[c] == stack[-1]:
                    stack.pop()
                    continue
            
                else:
                    return False

        if len(stack) == 0:
            return True
        
        return False