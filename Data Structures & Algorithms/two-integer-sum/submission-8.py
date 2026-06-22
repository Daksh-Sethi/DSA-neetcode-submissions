class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            if (target - nums[i]) in hashset and i!=hashset[target-nums[i]]:
                return [i,hashset[target-nums[i]]] 
               
