class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        output = ""
        result = ""

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                output = output[1:]

            seen.add(s[right])
            output += s[right]
            result = max(result, output, key=len)

        return len(result)