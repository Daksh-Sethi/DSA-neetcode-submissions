class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        output = ""
        max_output = ""

        i = 0

        while i < len(s):
            if s[i] not in seen:
                seen.add(s[i])
                output += s[i]
                i += 1
            else:
                while output and s[i] in seen:
                    seen.remove(output[0])
                    output = output[1:]

                seen.add(s[i])
                output += s[i]
                i += 1

            if len(output) > len(max_output):
                max_output = output


        return len(max_output)


