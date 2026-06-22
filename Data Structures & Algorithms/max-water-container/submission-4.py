class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        n=len(heights)
        max_area=0
        for i in range(n-1):
            for j in range(1,n):
                area = (j-i)*min(heights[i],heights[j])
                if(area>max_area):
                    max_area=area
        return max_area