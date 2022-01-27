import sys


with open(sys.argv[1], 'r') as f:
    nums = [i for i in map(int, f.readlines())]
nums.sort()

if len(nums) % 2 == 0:
    median = (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) // 2
else:
    median = nums[len(nums) // 2]

answer = 0
for i in nums:
    answer += abs(median - i)

print(answer)
