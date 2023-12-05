'''Given N items where each item has some weight and profit 
associated with it and also given a bag with capacity W, [i.e., 
the bag can hold at most W weight in it]. The task is to put the 
items into the bag such that the sum of profits associated with them is the maximum possible. '''

# Using Dynammic programming
def knapsack_01(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
print(knapsack_01(values, weights, W))
