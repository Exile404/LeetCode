buyPrice = float('inf')
    maxProfit = 0
    
    for price in prices:
        buyPrice = min(buyPrice, price)
        profit = price - buyPrice
        maxProfit = max(maxProfit, profit)
    
    return maxProfit
