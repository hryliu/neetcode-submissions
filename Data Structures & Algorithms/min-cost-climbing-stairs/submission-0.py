class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        num_steps = len(cost) 
        dp = [0] * (num_steps + 1)
        dp[1], dp[2] = cost[0], cost[1]

        for i in range(3, num_steps + 1):
            # choose cheapest way to get to step
            dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])

        return min(dp[num_steps], dp[num_steps - 1])