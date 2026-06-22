class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = set()
        for i in nums:
            if i in array:
                return True
            array.add(i)
        return False
        