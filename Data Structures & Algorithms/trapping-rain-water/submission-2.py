class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        suffix = []
        n=len(height)-1
        maxi = height[0]
        for i in range(1,n+1):
            prefix.append(maxi)
            if height[i] > maxi:
                maxi = height[i]
            
        
        maxi=height[n]
        for i in range(n-1,-1,-1):
            suffix.append(maxi)
            if height[i] > maxi:
                maxi = height[i]
        suffix= suffix[::-1]    
        suffix.append(0)

        trap = 0
        for i in range(1,n):
            if height[i]<suffix[i] and height[i]<prefix[i]:
                trap = trap + min(prefix[i],suffix[i])-height[i]
        
        return trap
            

        