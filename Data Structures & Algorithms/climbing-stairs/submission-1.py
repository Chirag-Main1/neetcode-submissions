class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        cache= [1,2]
        i = 3
        while i <= n:
            tmp = cache[1]
            cache[1] = cache[1] + cache[0]
            cache[0] = tmp
            i+=1
        return cache[1]

        # cache = {}
        # def dp(n,cache):
        #     if n in cache:
        #         return cache[n]
            
        #     if n == 0:
        #         return 1
        #     if n<0:
        #         return 0
            
        #     cache[n] = dp(n-1,cache) + dp(n-2,cache)
        #     return cache[n]
        
        # return dp(n,cache)