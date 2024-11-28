class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lenn = len(digits)

        if lenn == 0:
            return []

        root = TrieNode()

        root.children['2'] = ['a', 'b', 'c']
        root.children['3'] = ['d', 'e', 'f']
        root.children['4'] = ['g', 'h', 'i']
        root.children['5'] = ['j', 'k', 'l']
        root.children['6'] = ['m', 'n', 'o']
        root.children['7'] = ['p', 'q', 'r', 's']
        root.children['8'] = ['t', 'u', 'v']
        root.children['9'] = ['w', 'x', 'y', 'z']

        res = []

        def bTrack(index, cStr):
            if len(cStr) == len(digits):
                res.append(cStr)
                return 

            for c in root.children[digits[index]]:
                    bTrack(index + 1, cStr + c)

        bTrack(0, "")
        return res