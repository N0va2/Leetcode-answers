class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * n
    left = 0
    right = n - 1

    for i in range(n-1, -1, -1):
      square = 0
      if(abs(nums[left]) < abs(nums[right]):
        square = nums[right]
        right -= 1
      else:
        square = nums[left]
        left += 1
      ans[i] = square*square

    return ans
