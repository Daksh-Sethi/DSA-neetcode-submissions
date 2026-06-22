class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        output=""
        while(True):
            if i==len(strs[0]):
                return output
            output=output + strs[0][i]
            for j in range(1,len(strs)):
                if len(strs[j])==i or output[-1]!=strs[j][i] :
                    return output[:-1]
            i=i+1
