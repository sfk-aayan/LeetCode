class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = deque(), deque()
        for i in range(len(senate)):
            r.append(i) if senate[i] == 'R' else d.append(i)

        while r and d:
            r_index = r.popleft()
            d_index = d.popleft()

            if r_index < d_index:
                r.append(r_index+len(senate))
            elif d_index < r_index:
                d.append(d_index + len(senate))

        return 'Radiant' if r else 'Dire'