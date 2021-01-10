# Leetcode : Best Time to Buy and Sell Stock II
""" Key point: 
    Example [1,2,3,4,5]
    Best case ) buy day 1(price 1) and sell day 5(price 5) which makes profit 4.
    But the thing is buy day 1 and sell day 5 is same as 
    buy 1 sell 2 + buy 2 sell 3 + buy 3 sell 4 + buy 4 and sell 5. 
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 
        profit = 0
        
        for i in range(1, len(prices)):
            if (prices[i] > prices[i-1]):
                profit += prices[i] - prices[i-1]
                
        return profit
                
        
        