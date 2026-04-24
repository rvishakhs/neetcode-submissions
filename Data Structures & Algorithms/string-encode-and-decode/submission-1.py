class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for i in strs:
            res += str(len(i)) + "£" + i
        return res 

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res, i = [], 0
        while i < len(s):
            num = ""
            while s[i] != "£":
                num += s[i]
                i += 1
            num = int(num)
            res.append(s[i+1:i+num+1])
            i += num +1
        return res

