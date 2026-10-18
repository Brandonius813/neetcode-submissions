class Solution:
    def isValid(self, s: str) -> bool:

        # Keep track of "Open" sets and "most recent open"
        # If the close is equal tot he most recent open, we're good.
            # IF this is NOT TRUE, then we're cooked.  False.  This catches both out of order and also closing before opening

        # This seems like a stack situation.  Put the opens in a stack.  If we have closed = open all the way down the stack and stack is empty, return true.

        # The trick I didnt know was making a hashmap to connect closes to opens

        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(c)
        
        return True if not stack else False
                
