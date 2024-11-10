class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1 

        adj = collections.defaultdict(list)
        
        def strCmp(str1, str2):
            ct = 0

            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    ct +=1

            return ct == 1

        bLen = len(bank)
        for i in range(bLen):
            for j in range(i+1, bLen):
                if strCmp(bank[i], bank[j]) == 1:
                    adj[bank[i]].append(bank[j])

        for item in bank:
            if strCmp(startGene, item) == 1:
                adj[startGene].append(item)

        moves = 0
        q = collections.deque()
        visit = set()
        q.append((startGene, moves))

        while q:
            gene, moves = q.popleft()
            visit.add(gene)

            if gene == endGene:
                return moves

            for item in adj[gene]:
                if item not in visit:
                    q.append((item, moves + 1))

        return -1