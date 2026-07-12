class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}
        def dp(n,cache):
            if n in cache:
                return cache[n]
            
            if n == 0:
                return 1
            if n<0:
                return 0
            
            cache[n] = dp(n-1,cache) + dp(n-2,cache)
            return cache[n]
        
        return dp(n,cache)
        