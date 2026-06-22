class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={char:0 for char in s}
        for char in s:
            s_dict[char]=s_dict[char]+1
        t_dict={char:0 for char in t}
        for char in t:
            t_dict[char]=t_dict[char]+1
        if(s_dict==t_dict):
            return True
        return False
