class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)
        def dp(index, cache):
            if index in cache:
                return cache[index]
            
            if index >= n:
                return 0

            # if dp(index+1,cache)<dp(index+2,cache):
            #     cache[index] = cost[index] + dp(index+1,cache)
            # else:
            #     cache[index] = cost[index] + dp(index+2,cache)
            cache[index] = cost[index] + min(dp(index+2,cache),dp(index+1,cache))            
            return cache[index]
        
        return min(dp(0,cache), dp(1,cache))