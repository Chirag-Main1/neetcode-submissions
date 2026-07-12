class Solution:
    def tribonacci(self, n: int) -> int:
        # cache = {}
        # def dp(i,cache):
        #     if i<=1 :
        #         return i
        #     if i == 2:
        #         return 1
            
        #     if i in cache:
        #         return cache[i]
            
        #     cache[i] = dp(i-1,cache) + dp(i-2,cache) + dp(i-3,cache)
        #     return cache[i]
        
        # return dp(n,cache)
        if n<=1:
            return n
        if n==2:
            return 1


        dp = [0,1,1]
        i = 3
        while i <= n:
            tmp = dp[1]
            tmp1 = dp[2]
            val = dp[0] + dp[1] + dp[2]
            dp[2] = val
            dp[0] = tmp
            dp[1] = tmp1
            i+=1
        return(dp[2])
        
        