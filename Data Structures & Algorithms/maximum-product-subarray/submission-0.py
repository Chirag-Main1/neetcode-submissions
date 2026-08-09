class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # n = len(nums)
        # m = float("-inf")
        # for i in range(n):
        #     if nums[i]>m:
        #         m = nums[i]
        #     temp = nums[i]
        #     for j in range(i+1,n):
        #         if (temp*nums[j]) >= m:
        #             m = temp*nums[j]
        #         temp = temp*nums[j]
                
        # return m
        curr_max = 1
        curr_min = 1
        result = float("-inf")

        for i in nums:
            
            tmp = curr_max

            curr_max = max(curr_max*i,curr_min*i,i)
            curr_min = min(tmp*i,curr_min*i,i)
        
            result = max(result,curr_max)
        
        return result

