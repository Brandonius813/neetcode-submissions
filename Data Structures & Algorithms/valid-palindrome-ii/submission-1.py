class Solution:
    def validPalindrome(self, s: str) -> bool:
        # If 2 characters are unequal, is everything to the left/right a palindrome?  If one direction is yes, then return true and end there.  If neither is yes, then return false.  If there's no deletion, 2 pointers keep rolling until they finish the string.

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # Reverse s[l:], check against s[l:].  Repeat for s[:r+1]
                skipL, skipR = s[l + 1:r + 1], s[l:r]
                return (skipL == skipL[::-1]
                        or skipR == skipR[::-1])

            l += 1
            r -= 1
        
        return True