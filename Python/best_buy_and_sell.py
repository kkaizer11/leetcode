def maxProfit(prices):
    min = prices[0]
    pos = 0
    for i in range(len(prices)):
        if prices[i] < min:
            min = prices[i]
            pos = i
    profitable = prices[pos:]
    return(max(profitable) - min)


# prices = [7,6,4,3,1]
# maxProfit(prices)