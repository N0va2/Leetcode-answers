class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = dict()
        count[0] = -1

        maxlen = count_diff = 0

        for i, num in enumerate(nums):
            count_diff += 1 if num == 1 else -1
            if count_diff in count:
                maxlen = max(maxlen, i-count[count_diff])
            else:
                count[count_diff] = i
        
        return maxlen
