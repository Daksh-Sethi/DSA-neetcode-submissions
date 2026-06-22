class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i=0
        # while(i<len(nums)-1):
        #     if(nums[i]==nums[i+1]):
        #         nums.pop(i+1)
        #         continue
        #     i=i+1
        # return len(nums)
        i=0
        j=1
        while(j<len(nums)):
            if(nums[i]!=nums[j]):
                i=i+1
                nums[i]=nums[j]
                j=j+1
            else:
                j=j+1
        return i+1
