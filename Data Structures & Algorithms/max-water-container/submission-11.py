class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i=0
        j=n-1
        area = max_area = 0
        while i<j:
            area = min(heights[i],heights[j]) * (j-i)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
            max_area = max(max_area,area)

        return max_area

        

