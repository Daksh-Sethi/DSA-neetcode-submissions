class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix = [0]
        n=len(prices)
        mini=prices[0]
        for i in range(1,n):
            prefix.append(mini)
            if prices[i] < mini:
                mini = prices[i]


        price = max_price =0
        for j in range(1,n):
            price = prices[j]-prefix[j]
            if price>max_price:
                max_price = price

        if(max_price<0):
            return 0

        return max_price