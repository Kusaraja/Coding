class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            l[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            l[i] *= suffix
            suffix *= nums[i]
        return l

