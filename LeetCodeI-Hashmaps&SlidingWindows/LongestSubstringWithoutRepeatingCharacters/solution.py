class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        freq = {}

        for end in range(len(s)):
            if s[end] in freq:
                freq[s[end]] += 1
            else:
                freq[s[end]] = 1

            while freq[s[end]] > 1:
                freq[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
