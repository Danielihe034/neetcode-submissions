class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxPrice = 0
        while (r < len(prices)):
            if prices[l] < prices[r]:
                current = prices[r] - prices[l]
                maxPrice = max(maxPrice, current)
            else: 
                prices[l] > prices[r]
                l = r
            r += 1
        return maxPrice

            

            
        