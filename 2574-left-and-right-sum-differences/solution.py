class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            leftsum = sum(nums[:i])
            rightsum = sum(nums[i+1:])
            ans.append(abs(leftsum - rightsum))
        return ans