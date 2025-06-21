class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        ct = 0
        prev = 0

        if flowerbed[prev] == 0 and prev+1 < len(flowerbed) and flowerbed[prev+1] != 1:
            flowerbed[prev] = 1
            ct += 1

        for nxt in range(1, len(flowerbed)-1):
            if flowerbed[nxt] != 1 and flowerbed[prev] != 1 and flowerbed[nxt+1] != 1:
                flowerbed[nxt] = 1
                ct += 1
            prev += 1

        if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
            flowerbed[len(flowerbed)-1] = 1
            ct += 1
        
        return ct >= n
        