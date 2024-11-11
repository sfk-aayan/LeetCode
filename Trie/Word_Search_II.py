class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        def addNode(root, word):
            cur = root

            for c in word:
                index = ord(c) - ord('a')

                if not cur.children[index]:
                    cur.children[index] = TrieNode()

                cur = cur.children[index]

            cur.isLeaf = True

        for word in words:
            addNode(root, word)

        rows, cols = len(board), len(board[0])
        visit, result = set(), set()
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        def dfs(r, c, node, word):

            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or not node.children[ord(board[r][c])-ord('a')]:
                return

            visit.add((r, c))
            index = ord(board[r][c]) - ord('a')
            node = node.children[index]
            word += board[r][c]

            if node.isLeaf:
                result.add(word)

            for x, y in directions:
                rw, cl = r + x, c + y
                dfs(rw, cl, node, word)

            visit.remove((r, c))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")

        return list(result)


        