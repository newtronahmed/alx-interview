#!/usr/bin/env python3
"""make change module"""


def makeChange(coins, total):
    """determine the fewest number of coins needed"""
    if total < 0:
        return -1

    # Initialize a table to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Update the table for each coin value
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the final entry in the table is still infinity, no combination is possible
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
