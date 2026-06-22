class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for k in range(n - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue  # skip duplicate first elements

            if nums[k] > 0:
                break  # no way to sum to 0 anymore

            i, j = k + 1, n - 1

            while i < j:
                total = nums[k] + nums[i] + nums[j]

                if total == 0:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1

                    # skip duplicates
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif total < 0:
                    i += 1
                else:
                    j -= 1

        return res