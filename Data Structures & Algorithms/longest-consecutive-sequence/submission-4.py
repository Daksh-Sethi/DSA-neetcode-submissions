class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        nums = sorted(nums)
        count = 1
        output = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                count+=1
            else:
                output = max(output, count)
                count=1

        return max(output, count)

        # 2,3,4,4,5,10,20
        # 0,1,1,2,3,4,5,6