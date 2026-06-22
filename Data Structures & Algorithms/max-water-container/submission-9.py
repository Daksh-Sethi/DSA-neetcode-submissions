class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_area=0
        while(i<j):
            area = (j-i)*min(heights[i],heights[j])
            if(area>max_area):
                max_area=area
            if(heights[i]<heights[j]):
                i=i+1
                continue
            if(heights[i]>heights[j]):
                j=j-1
                continue
            
            i=i+1
            j=j-1
        return max_area