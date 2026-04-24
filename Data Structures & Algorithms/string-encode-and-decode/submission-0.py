class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        size_list = []
        single_str = ""
        for s in strs:
            size_list.append(len(s))
        for sz in size_list:
            single_str += str(sz)
            single_str += ','
        single_str += '#'
        for s in strs:
            single_str += s

        return single_str
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res


