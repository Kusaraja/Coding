class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1]+nums[i]
        total = prefix[n-1]
        diff = 0
        c = 0
        for i in range(n-1):
            rightsum = total-prefix[i]
            leftsum = prefix[i]
            diff = abs(rightsum - leftsum)
            if diff % 2 == 0:
                c += 1
                print(diff)
        return c