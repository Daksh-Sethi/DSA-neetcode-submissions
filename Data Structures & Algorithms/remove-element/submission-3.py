class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=0
        n=len(nums)
        while(i<n-j):
            if(nums[i]==val):
                nums[i],nums[n-j-1]=nums[n-j-1],nums[i]
                i=i-1
                j=j+1
            i=i+1
        return (n-j)
