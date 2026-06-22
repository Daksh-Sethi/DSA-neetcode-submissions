class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        product = 1
        for i in range(1,len(nums)):
            product*=nums[(i-1)]
            prefix.append(product)
        
        product = 1
        suffix = []
        nums2=nums[::-1]
        for i in range(1,len(nums[::-1])):
            product*=nums2[i-1]
            suffix.append(product)
        suffix = suffix[::-1]
        suffix.append(1)

        output=[]
        for i in range(len(nums)):
            output.append(prefix[i]*suffix[i])

        return output

