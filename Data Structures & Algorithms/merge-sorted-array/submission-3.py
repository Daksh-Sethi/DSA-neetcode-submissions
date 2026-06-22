class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i=j=0
        
        # while(i<m+n and j<n):
        #     if(i>=m+j):
        #         nums1.pop()
        #         nums1.insert(i,nums2[j])
        #         i=i+1
        #         j=j+1
        #     elif(nums1[i]>nums2[j]) :
        #         nums1.pop()
        #         nums1.insert(i,nums2[j])
        #         j=j+1
        #         i=i+1
        #     else:
        #         i=i+1
        i=m-1
        j=n-1
        k=m+n-1
        while i>=0 and j>=0:
            if (nums1[i]>=nums2[j]):
                nums1[k]=nums1[i]
                i=i-1
                k=k-1
            else:
                nums1[k]=nums2[j]
                j=j-1
                k=k-1
        while j>=0:
            nums1[k]=nums2[j]
            k=k-1
            j=j-1
        