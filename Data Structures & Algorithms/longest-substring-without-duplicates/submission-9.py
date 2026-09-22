class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_len = 0
        l = 0

        for r in range(len(s)):
            curr = s[r]

            if curr in char_map and char_map[curr] >= l:
                l = char_map[curr] + 1

            char_map[curr] = r
            max_len = max(max_len, r - l + 1)
        return max_len