class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        seen = set()
        for i in range(len(nums)-2):
            target = -nums[i]
            k=i+1
            j=len(nums)-1
            while(j>k):
                if(target == nums[k]+nums[j]):
                    size = len(seen)
                    triplet = [nums[i],nums[j],nums[k]]
                    triplet.sort()
                    seen.add(tuple(triplet))
                    if(len(seen)>size):
                        output.append([nums[i],nums[j],nums[k]])
                    if(nums[j-1]==nums[j]):
                        j=j-1
                        continue
                    elif(nums[k]==nums[k+1]):
                        k=k+1
                        continue
                    k=k+1
                    j=j-1

                elif(target < nums[k]+nums[j]):
                    j=j-1
                
                elif(target > nums[k]+nums[j]):
                    k=k+1

        return output

