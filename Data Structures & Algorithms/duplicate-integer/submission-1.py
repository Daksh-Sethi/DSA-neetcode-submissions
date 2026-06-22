class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {key: 0 for key in nums}
        for i in nums:
            a[i]=a[i]+1
            if a[i]>1:
                return True
        return False
        