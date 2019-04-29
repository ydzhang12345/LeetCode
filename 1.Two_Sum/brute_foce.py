# O(n^2) brute force
class Solution:
    def twoSum(self, nums, target: int):
    	for i, v in enumerate(nums):
			for j in range(i+1, len(nums)):
				if v+nums[j]==target:
					return [i, j]
sol = Solution()
print(sol.twoSum([4,2,6], 6))
