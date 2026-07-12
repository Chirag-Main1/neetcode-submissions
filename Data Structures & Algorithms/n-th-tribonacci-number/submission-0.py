class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        def dp(i,cache):
            if i<=1 :
                return i
            if i == 2:
                return 1
            
            if i in cache:
                return cache[i]
            
            cache[i] = dp(i-1,cache) + dp(i-2,cache) + dp(i-3,cache)
            return cache[i]
        
        return dp(n,cache)

        
        