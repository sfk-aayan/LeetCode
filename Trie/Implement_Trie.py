class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for letter in word:
            index = ord(letter) - ord('a')

            if not cur.children[index]:
                cur.children[index] = TrieNode()

            cur = cur.children[index]

        cur.isLeaf = True
        
    def search(self, word: str) -> bool:
        cur = self.root

        for letter in word:
            index = ord(letter) - ord('a')

            if not cur.children[index]:
                return False

            cur = cur.children[index]

        return cur.isLeaf

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for letter in prefix:
            index = ord(letter) - ord('a')

            if not cur.children[index]:
                return False

            cur = cur.children[index]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)