class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        hasher = len(strs) + 1
        ascii_vals = ""

        for word in strs:
            if not word:
                ascii_vals += "."
                continue

            for char in word:
                val = ord(char) * hasher
                ascii_vals += str(val) + ","

            ascii_vals = ascii_vals[:-1] + "."

        return ascii_vals

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        words = s[:-1].split(".")
        hasher = len(words) + 1
        dec = []

        for word in words:
            if not word:
                dec.append("")
                continue
            
            chars = []
            for val in word.split(","):
                act = int(val) // hasher
                chars.append(chr(act))
            dec.append("".join(chars))
            
        return dec