class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        cache1 = {}
        if len(nums)==1:
            return nums[0]
        def dp(n,cache,nums):
            p = len(nums)
            if n >= p:
                return 0
            if n in cache:
                return cache[n]

            cache[n] = max((nums[n]+dp(n+2,cache,nums)),dp(n+1,cache,nums))
            return cache[n]

        nums1 = nums[1:]
        nums2 = nums[:-1]
        print(nums2)
        return max(dp(0,cache,nums1),dp(0,cache1,nums2))
        
        