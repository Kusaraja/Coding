class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        c = 0
        total = sum(nums)
        for i in range(n-1):
            prefix += nums[i]
            leftsum =  prefix
            rightsum = total - leftsum
            diff = abs(rightsum-leftsum)
            print(diff)
            if diff % 2 == 0:
                c += 1
        return c