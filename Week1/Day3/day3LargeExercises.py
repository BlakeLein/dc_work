# Tic Tac Toe GRID


# Validate Subsequence:


# Two Number Sum:
nums = nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    for i in range(len(nums)):
                for j in range(i, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]

print(twoSum(nums, target))

# Three Number Sum:
list = [12, 3, 1, 2, -6, 5, -8, 6]