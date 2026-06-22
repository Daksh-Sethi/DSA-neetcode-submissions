class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        seen = set()
        n=len(s)
        output=0
        while(j<n):
            if s[j] in seen:
                while(s[j]!=s[i]):
                    seen.remove(s[i])
                    i=i+1
                i=i+1
                j=j+1
                continue
            seen.add(s[j])
            if(len(seen)>output):
                output=len(seen)
            j+=1
        return output