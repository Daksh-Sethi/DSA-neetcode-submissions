class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict=[]
        for i in range(len(strs)):
            word={}
            for j in strs[i]:
                word[j]=word.get(j,0)+1
            strs_dict.append(word)
        
        output=[]
        for i in range(len(strs_dict)):
            if(strs_dict[i]=={-1:-1}):
                continue
            comb=[strs[i]]
            for j in range(i,len(strs_dict)):
                if i==j:
                    continue
                if strs_dict[i]==strs_dict[j]:
                    comb.append(strs[j])
                    strs_dict[j]={-1:-1}
            output.append(comb)
        return output
