class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count={num:0 for num in nums}
        for num in nums:
            count[num]=count[num]+1
        for key,value in count.items():
            if count[key]>1:
                return True
        return False
