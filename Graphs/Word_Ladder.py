class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def strCmp(str1, str2):
            ct = 0

            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    ct += 1

            return ct == 1

        adj = defaultdict(list)
        wordLen = len(wordList)

        for i in range(wordLen):
            for j in range(i+1, wordLen):
                if strCmp(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])

        for item in wordList:
            if strCmp(beginWord, item):
                adj[beginWord].append(item)

        q = deque()
        visit = set()
        moves = 1
        q.append((beginWord, moves))

        while q:
            word, moves = q.popleft()
            visit.add(word)

            if word == endWord:
                return moves

            for item in adj[word]:
                if item not in visit:
                    q.append((item, moves + 1))
       
        return 0
        