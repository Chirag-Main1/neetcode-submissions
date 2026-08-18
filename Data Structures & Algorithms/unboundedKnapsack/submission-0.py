class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        memo = {}

        def dfs(c):
            if c == 0:
                return 0

            if c in memo:
                return memo[c]

            max_profit = 0

            for i in range(len(weight)):
                if weight[i] <= c:
                    max_profit = max(
                        max_profit,
                        profit[i] + dfs(c - weight[i])
                    )

            memo[c] = max_profit
            return max_profit

        return dfs(capacity)