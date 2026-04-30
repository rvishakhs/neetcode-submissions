class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded = ""
        for char in strs:
            encoded += str(len(char)) + "#" + char
        return encoded
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res, i = [], 0
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            num = int(num)
            res.append(s[i+1: i+1+num])
            i += num + 1
        return res
