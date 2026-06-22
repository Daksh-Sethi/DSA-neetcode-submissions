class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        product_zero =False
        count = 0
        for i in nums:
            if i!=0:
                product = product * i
            else:
                count +=1
                product_zero = True
        output = []
        for i in nums:
            if count>1:
                output.append(0)
            elif i!=0 and product_zero == False:
                output.append(int(product/i))
            elif i!=0 and product_zero == True:
                output.append(0)
            elif i==0:
                output.append(product)

        return output
