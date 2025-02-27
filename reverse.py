# Take user input as space-separated values and convert to a list of integers
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Initialize pointers
left, right = 0, len(nums) - 1

# Swap elements using two-pointer approach
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

# Print the reversed list
print("Reversed List:", nums)

