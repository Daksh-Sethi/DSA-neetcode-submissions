class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs={}
        for i in range(len(nums)):
            pairs[target-nums[i]]=i
        for i in range(len(nums)):
            if pairs.get(nums[i],-1)==-1:
                continue
            elif i==pairs.get(nums[i]):
                continue
            return [i,pairs.get(nums[i])]
        
