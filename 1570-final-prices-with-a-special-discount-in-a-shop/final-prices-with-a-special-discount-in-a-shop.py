class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Initialize an empty list to store the final prices
        final_prices = []
        
        # Loop through each item in the prices array
        for i in range(len(prices)):
            discount = 0
            # Loop through the subsequent items to find the discount
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            
            # Append the price minus the discount to the final prices
            final_prices.append(prices[i] - discount)
        
        return final_prices
