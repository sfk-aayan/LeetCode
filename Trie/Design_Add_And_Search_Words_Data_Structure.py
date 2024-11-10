class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for letter in word:
            index = ord(letter) - ord('a')

            if not cur.children[index]:
                cur.children[index] = TrieNode()

            cur = cur.children[index]

        cur.isLeaf = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):

                c = word[i]

                if c == '.':
                    for child in cur.children:
                        if child:
                            if dfs(i + 1, child):
                                return True

                    return False

                else:
                    index = ord(c) - ord('a')
                    if not cur.children[index]:
                        return False
                    cur = cur.children[index]

            return cur.isLeaf

        return dfs(0, self.root)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)