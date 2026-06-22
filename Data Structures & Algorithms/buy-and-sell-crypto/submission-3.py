class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        n=len(prices)
        mini=100
        profit=0
        while(j<n):
            if prices[i]<mini:
                mini=prices[i]
            if prices[j]-mini>profit:
                profit = prices[j]-mini
            i+=1
            j+=1
        return profit 
                

