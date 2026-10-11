class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        n = len(nums)
        for i in range(n):
            if target-nums[i] in m:
                return [m[target-nums[i]],i]
            m[nums[i]] = i
            