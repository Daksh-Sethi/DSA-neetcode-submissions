class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 1
        output = 1
        if(len(nums)==0):
            return 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                count+=1
            else:
                if output<count:
                    output=count
                count=1

        if output<count:
            output = count
        return output

        # 2,3,4,4,5,10,20
        # 0,1,1,2,3,4,5,6