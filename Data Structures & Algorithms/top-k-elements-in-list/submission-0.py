class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={i:0 for i in nums}
        for i in nums:
            d[i]+=1
        top_k = sorted(d, key=d.get, reverse=True)[:k]
        return top_k