class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        lis = []
        l = 0
        for i in range(n):
            k = i+1
            if n % k == 0:
                m = nums[i] * nums[i]
                lis.append(m)
                l += m
        print(lis)
        return l