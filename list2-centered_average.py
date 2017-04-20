def centered_average(nums):
  #centered_sum = sum(nums) - min(nums) - max(nums)
  #return centered_sum / (len(nums)-2)
  min_num = 2**63 - 1
  max_num = -2**63
  nums_sum = 0
  for num in nums:
    if num > max_sum:
      max_sum = num
    if num < min_num:
      min_num = num
    mysum += num
  centered_average = (mysum - mymin - mymax) / (len(nums) - 2)
  return centered_average
