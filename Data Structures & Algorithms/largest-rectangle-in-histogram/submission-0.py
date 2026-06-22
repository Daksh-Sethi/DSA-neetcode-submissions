class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        prev = [0] * n

        for i in range(1, n):
            j = i - 1

            while j >= 0 and heights[j] >= heights[i]:
                prev[i] += prev[j] + 1
                j -= prev[j] + 1

        print(prev)

        suf = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1

            while j < n and heights[j] >= heights[i]:
                suf[i] += suf[j] + 1
                j += suf[j] + 1

        print(suf)
        area=[]
        for i in range(n):
            area.append((prev[i]+suf[i]+1)*heights[i])
        return(max(area))