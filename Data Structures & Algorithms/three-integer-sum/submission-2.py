class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums) - 2):
            # Skip duplicate `i`
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            k = i + 1
            j = len(nums) - 1
            while k < j:
                s = nums[k] + nums[j]
                if s == target:
                    output.append([nums[i], nums[k], nums[j]])
                    k += 1
                    j -= 1
                    # Skip duplicate `k`
                    while k < j and nums[k] == nums[k-1]:
                        k += 1
                    # Skip duplicate `j`
                    while k < j and nums[j] == nums[j+1]:
                        j -= 1
                elif s < target:
                    k += 1
                else:
                    j -= 1
        return output
