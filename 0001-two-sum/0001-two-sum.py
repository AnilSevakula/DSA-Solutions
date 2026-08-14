class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute Force
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        #Optimised
        seen = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen:
                return [i, seen[comp]]
            seen[nums[i]] = i
        return []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna