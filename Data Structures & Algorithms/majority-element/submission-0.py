class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        no = len(nums)
        for key,val in count.items():
            if(val>int(no/2)):
                return key