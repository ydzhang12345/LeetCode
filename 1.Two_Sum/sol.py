# think it in a backward way
# O(n) python hash list
import pdb
class Solution:
    def twoSum(self, nums, target: int):
    	seen = {}
    	for i, v in enumerate(nums):
    		diff = target - v
    		if diff in seen:
    			return [seen[diff], i]
    		else:
    			seen[v] = i

sol = Solution()
print(sol.twoSum([0,4,2,0], 0)) 

