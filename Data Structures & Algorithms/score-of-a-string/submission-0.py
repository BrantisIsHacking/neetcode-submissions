class Solution:
    def scoreOfString(self, s: str) -> int:
        x = 0
        score = 0

        while x < len(s) - 1:
            score += abs(ord(s[x]) - ord(s[x + 1]))
            x += 1
        
        return score