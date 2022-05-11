l= list(map(int, input()))

nums = [0]*10

for i in l:
  nums[i] += 1
  
nums[6] += nums[9]
nums[6] = nums[6]//2 + nums[6]%2
nums[9] = 0

print(max(nums))