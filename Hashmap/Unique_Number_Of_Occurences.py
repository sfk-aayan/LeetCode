class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hMap = collections.defaultdict(int)

        for item in arr:
            hMap[item] += 1

        ct = set()
        for value in hMap.values():
            if value in ct:
                return False
            else:
                ct.add(value)

        return True
