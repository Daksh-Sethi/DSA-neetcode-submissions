class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output=[]
        for k in range(len(nums)):
            i=k+1
            j=len(nums)-1
            while i<j:
                if nums[i] + nums[j] + nums[k]== 0  :
                    if [nums[k],nums[i],nums[j]] not in output:
                        output.append([nums[k],nums[i],nums[j]])
                    i+=1
                    j-=1
                elif nums[i] + nums[j] + nums[k]<0 :
                    i+=1
                else:
                    j-=1
        return output
