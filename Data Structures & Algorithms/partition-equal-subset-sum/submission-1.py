class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        cache = {}

        def part(i, s):
            if s == target:
                return True

            if i >= len(nums) or s > target:
                return False

            if (i, s) in cache:
                return cache[(i, s)]

            cache[(i, s)] = (
                part(i + 1, s + nums[i]) or
                part(i + 1, s)
            )

            return cache[(i, s)]

        return part(0, 0)