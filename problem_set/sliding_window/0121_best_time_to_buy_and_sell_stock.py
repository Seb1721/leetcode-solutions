from typing import List

# 8/31/26
# Problem 121: Best Time to Buy and Sell Stock
# Difficulty: Easy

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different
# day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Logic:
    # Keep track of the lowest price seen so far as a possible buy price.
    # For each price, calculate the profit if you sold on that day.
    # If that profit is better than the best one so far, update max_profit.
    # Return the best profit found, or 0 if no profit is possible.

# Complexity:
    # Time: O(n)
    # Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        # Track the lowest buy price seen so far, then compare the profit from selling today.
        for price in prices:
            if price < min_price:
                min_price = price

            current_profit = price - min_price

            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
