class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        total = sum(nums)
        rightsum = 0
        leftsum = 0
        for num in nums:
            rightsum = total - num - leftsum
            ans.append(abs(leftsum - rightsum))
            leftsum += num
        return ans