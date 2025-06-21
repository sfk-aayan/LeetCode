class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        insert = 0
        while i < len(chars):
            j = i + 1
            ct = 1
            while j < len(chars) and chars[i] == chars[j]:
                ct += 1
                j += 1
            chars[insert] = chars[i]
            insert += 1
            if ct > 1:
                n = str(ct)
                chars[insert: insert+len(n)] = list(n)
                insert += len(n)

            i += ct
        return insert
