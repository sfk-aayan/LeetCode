class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = collections.defaultdict(list)

        result = []

        for item in strs:
            temp = sorted(item)
            temp = ''.join(temp)
            hMap[temp].append(item)

        for values in hMap.values():
            result.append(values)

        return result