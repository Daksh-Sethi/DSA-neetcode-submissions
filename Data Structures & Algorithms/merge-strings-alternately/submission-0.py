class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i = j = 0
        s = ""
        while(i<n and j<m):
            s=s+word1[i]
            s=s+word2[j]
            i=i+1
            j=j+1
        
        while(i<n):
            s=s+word1[i]
            i=i+1
        while(j<m):
            s=s+word2[j]
            j=j+1

        return s