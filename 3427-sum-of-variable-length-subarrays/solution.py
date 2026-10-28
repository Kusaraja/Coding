class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        start = 0
        s = 0
        for i in range(len(nums)):
            start = max(0,i-nums[i])
            print(start)
            s += sum(nums[start:i+1])
            print("sum:",s)
        return s