class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(ch.lower() for ch in s if ch.isalnum())
        j=len(result)-1
        for i in range(len(result)//2):
            if result[i]==result[j]:
                i+=1
                j-=1
            else:
                return False
        return True