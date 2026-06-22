class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        product = 1
        for i in range(1,len(nums)):
            product*=nums[(i-1)]
            prefix.append(product)
        
        suffix = [1] * len(nums)
        product = 1

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = product
            product *= nums[i]

        output=[]
        for i in range(len(nums)):
            output.append(prefix[i]*suffix[i])

        return output

