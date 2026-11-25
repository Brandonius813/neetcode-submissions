# 2 pointers, ignore punctuation and spaces.
# The trick is 'is this alphanumeric' - use method .isalpha()

# Missed the part where I gotta upper/lower both characters.

# Failed to do isalnum, used is alpha instead

# Failed to account for edge case where my alphanumeric check pushes a pointer out of bounds

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:

            while l < len(s) and s[l].isalnum() == False:
                l += 1
            
            while r > 0 and s[r].isalnum() == False:
                r -= 1
            
            if l > len(s) or r <= 0:
                break
            
            if s[l].lower() != s[r].lower():
                return False
            
            else:
                l += 1
                r -= 1
        
        return True

