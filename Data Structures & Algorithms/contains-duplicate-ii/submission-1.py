class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=1
        n=len(nums)
        while(j<n):
            if(nums[i]==nums[j]):
                return True
            j=j+1
            if(j-i)>k:
                i=i+1
        return False