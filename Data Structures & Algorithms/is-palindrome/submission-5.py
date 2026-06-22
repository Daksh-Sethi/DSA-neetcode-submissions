class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(ch.lower() for ch in s if ch.isalnum())
        j=len(result)-1
        i=0
        while i<j:
            if result[i]==result[j]:
                i+=1
                j-=1
            else:
                return False
        return True