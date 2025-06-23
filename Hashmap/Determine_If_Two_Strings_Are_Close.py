class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        w1 = collections.defaultdict(int)
        w2 = collections.defaultdict(int)

        for i in range(len(word1)):
            w1[word1[i]] += 1
            w2[word2[i]] += 1

        return w1.keys() == w2.keys() and sorted(w1.values()) == sorted(w2.values())