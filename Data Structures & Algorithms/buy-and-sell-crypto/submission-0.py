class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxPrice = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                price = prices[r] - prices[l]
                maxPrice = max(price, maxPrice)
            
            else:
                l = r
            
            r += 1
        
        return maxPrice
