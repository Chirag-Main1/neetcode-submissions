class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        p = len(nums)
        def dp(n,cache):
            if n >= p:
                return 0
            if n in cache:
                return cache[n]

            cache[n] = max((nums[n]+dp(n+2,cache)),dp(n+1,cache))
            return cache[n]

        
        return dp(0,cache)
        
        