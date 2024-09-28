class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        result = []
        index = 0
        numSize = len(nums)

        if numSize == 0:
            return result
            
        nums.append(nums[numSize - 1])


        while index < numSize:

            if index == numSize:
                break

            start = nums[index]
            while nums[index + 1] - nums[index] == 1:
                index += 1

            end = nums[index]

            if start == end:
                result.append(f'{start}')
            else:
                string = f'{start}->{end}'
                result.append(string)
            index += 1

        return result




        