class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) # math.ceil is division rounded up - this way we know how many hours something takes, given the remaining time
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            
            else:
                l = k + 1
        
        return res
