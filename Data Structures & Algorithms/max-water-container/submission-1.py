# Attempted a re-solve on Nov 25

# Brute force - 2 pointers, check all pairs that match with bar 1, then all pairs that match bar 2 (only to right) and so on.
# This is O(n^2) - not gonna cut it.

# If I initialize 2 pointers at L/R I think it covers all the scenarios!  I had to double check this against Claude but I can't find any exceptions by hand and the logic makes sense.

# By about 20 minutes, I was ready to code the solution and confident there were no edge cases.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        
        res = 0

        while l < r:
            area = (r - l) * (min(heights[l], heights[r]))
            res = max(area, res)

            if heights[l] < heights[r]:
                l += 1
            
            else:
                r -= 1

        return res
        